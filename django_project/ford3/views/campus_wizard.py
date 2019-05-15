import os
from datetime import datetime
from collections import OrderedDict
from django.shortcuts import redirect, Http404, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse
from django.forms.models import model_to_dict
from formtools.wizard.views import CookieWizardView
from ford3.models import (
    Campus,
    CampusEvent,
    Provider
)


class CampusFormWizard(CookieWizardView):
    template_name = 'campus_form.html'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'photos'))
    new_campus_events = []

    @property
    def campus(self):
        campus_id = self.kwargs['campus_id']
        return get_object_or_404(
            Campus,
            id=campus_id)

    @property
    def provider(self):
        provider_id = self.kwargs['provider_id']
        return get_object_or_404(
            Provider,
            id=provider_id)

    def get(self, *args, **kwargs):
        if not self.campus or not self.provider:
            raise Http404()
        if 'step' in self.request.GET:
            return super().render_goto_step(self.request.GET['step'], **kwargs)
        else:
            return super(CampusFormWizard, self).get(*args, **kwargs)

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form, **kwargs)
        context['multi_step_form'] = True
        context['form_name_list'] = [
            'Details',
            'Location',
            'Important Dates',
            'Qualification Titles'
        ]
        context['campus'] = self.campus
        context['provider'] = self.provider
        context['provider_logo'] = self.provider.provider_logo.url \
            if self.provider.provider_logo else ""
        form_data = {
            'provider_name': self.provider.name
        }
        context['form_data'] = form_data

        if 'step' in self.request.GET:
            context['multi_step_form'] = False

        return context

    def get_form_initial(self, step):
        # For 'Details' and 'Location' forms
        initial_dict = model_to_dict(self.campus)

        # For 'Qualification Titles' form
        saqa_ids = ' '.join([
            str(s['saqa_qualification__id'])
            for s in self.campus.qualifications])

        initial_dict.update({'saqa_ids': saqa_ids})
        return initial_dict

    def done(self, form_list, **kwargs):
        for form in kwargs['form_dict']:
            cleaned_data = kwargs['form_dict'][form].cleaned_data

            if form == 'campus-details':
                self.campus.save_form_data(cleaned_data)
            elif form == 'campus-location':
                self.campus.save_postal_data(cleaned_data)
            elif form == 'campus-dates':
                self.campus.save_events(cleaned_data)
            elif form == 'campus-qualifications':
                self.campus.save_qualifications(cleaned_data)
                self.campus.delete_qualifications(cleaned_data)

        url = reverse('show-campus', args=(self.provider.id, self.campus.id))
        return redirect(url)

    def add_events(self, step_data, current_form):
        new_name = step_data['campus-dates-event_name']
        new_date_start = step_data['campus-dates-date_start']
        new_date_end = step_data['campus-dates-date_end']
        new_http_link = step_data['campus-dates-http_link']
        # Count how many names were submitted and create new_events
        number_of_new_events = len(new_name)
        if len(new_name) == 1 and new_name[0] == '':
            return False
        for i in range(0, number_of_new_events):
            new_campus_event = CampusEvent()
            new_campus_event.name = new_name[i]
            new_date_start_i = new_date_start[i]
            new_date_start_formatted = (
                datetime.strptime(new_date_start_i, '%m/%d/%Y')
            ).strftime('%Y-%m-%d')
            new_date_end_i = new_date_end[i]
            new_date_end_formatted = (
                datetime.strptime(new_date_end_i, '%m/%d/%Y')
            ).strftime('%Y-%m-%d')
            new_campus_event.date_start = new_date_start_formatted
            new_campus_event.date_end = new_date_end_formatted
            new_campus_event.http_link = new_http_link[i]
            self.new_campus_events.append(new_campus_event)

    def render_next_step(self, form, **kwargs):
        """
        This method gets called when the next step/form should be rendered.
        `form` contains the last/current form.
        """
        # get the form instance based on the data from the storage backend
        # (if available).


        if 'step' in self.request.GET:
            return self.render_done(form, **kwargs)
        else:
            return super().render_next_step(form, **kwargs)

    # def render(self, form=None, **kwargs):
    #     # print('am i here? render')
    #     form = form or self.get_form()
    #     context = self.get_context_data(form=form, **kwargs)


    #     current_step = context['view'].storage.current_step

    #     # TODO: Generate events from stored self.new_campus_events
    #     if current_step == 'campus-dates':
    #         self.new_campus_events = []

    #     # if context['multi_step_form'] is False:
    #     #         print('hello i render')
    #             # return self.render_done(form, **kwargs)
    #         # if context['current_form'] == 'campus-dates':


    #         # try:
    #         #     self.add_events(
    # context['view'].storage.data['step_data']['campus-dates'],
    #         #         form)
    #         # except KeyError:
    #         #     pass
    #     return self.render_to_response(context)


    def render_done(self, form, **kwargs):
        """
        This method gets called when all forms passed. The method should also
        re-validate all steps to prevent manipulation. If any form fails to
        validate, `render_revalidation_failure` should get called.
        If everything is fine call `done`.
        """
        final_forms = OrderedDict()

        if 'step' in self.request.GET:
            form_list = [self.request.GET['step']]
        else:
            form_list = self.get_form_list()

        # walk through the form list and try to validate the data again.
        for form_key in form_list:
            form_obj = self.get_form(
                step=form_key,
                data=self.storage.get_step_data(form_key),
                files=self.storage.get_step_files(form_key)
            )

            if not form_obj.is_valid():
                return self.render_revalidation_failure(
                    form_key, form_obj, **kwargs)
            final_forms[form_key] = form_obj

        # render the done view and reset the wizard before returning the
        # response. This is needed to prevent from rendering done with the
        # same data twice.
        done_response = self.done(
            final_forms.values(), form_dict=final_forms, **kwargs)
        self.storage.reset()

        return done_response
