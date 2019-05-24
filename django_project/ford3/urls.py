# coding=utf-8
from django.urls import path
from ford3.views import (
    views,
    saqa_qualifications,
    campus_events,
    user_management
)
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from ford3.forms.qualification import (
    QualificationDetailForm,
    QualificationDurationFeesForm,
    QualificationRequirementsForm,
    QualificationInterestsAndJobsForm,
    QualificationImportantDatesForm,
)
from ford3.views.qualification_wizard import QualificationFormWizard
from ford3.forms.campus import (
    CampusDetailForm,
    CampusLocationForm,
    CampusImportantDatesForm,
    CampusQualificationsForm
)
from ford3.views.campus_wizard import CampusFormWizard
from ford3.views import (
    campus,
    provider,
    sub_field_of_study,
    occupations
)
from ford3.forms.custom_auth_form import CustomAuthForm


qualification_wizard = QualificationFormWizard.as_view(
    [
        QualificationDetailForm,
        QualificationDurationFeesForm,
        QualificationRequirementsForm,
        QualificationInterestsAndJobsForm,
        QualificationImportantDatesForm,
    ],
)

CAMPUS_FORMS = [
    ('campus-details', CampusDetailForm),
    ('campus-location', CampusLocationForm),
    ('campus-dates', CampusImportantDatesForm),
    ('campus-qualifications', CampusQualificationsForm)
]

campus_wizard = CampusFormWizard.as_view(CAMPUS_FORMS)

urlpatterns = [
    path('providers/<int:provider_id>/',
         provider.show,
         name='show-provider'),
    path('providers/<int:provider_id>/edit/',
         provider.edit,
         name='edit-provider'),
    path(
        'providers/<int:provider_id>/campus/<int:campus_id>/edit/',
        campus_wizard,
        name='edit-campus'),
    path(
        'providers/<int:provider_id>/campus/<int:campus_id>/',
        campus.show,
        name='show-campus'),
    path(
        'providers/<int:provider_id>/campus/create/',
        campus.create,
        name='create-campus'),

    path(
        'campus/<int:campus_id>/events/',
        campus_events.create_or_update,
        name='create-or-update-campus-event'),
    path(
        'campus/events/delete/',
        campus_events.delete,
        name='delete-campus-event'),
    path(
        'saqa_qualifications/search/',
        saqa_qualifications.search,
        name='search-saqa-qualifications'),

    path(
        'saqa_qualifications/create/',
        saqa_qualifications.create,
        name='create-saqa-qualification'),
    path(
        '/'.join([
            'providers/<int:provider_id>',
            'campus/<int:campus_id>',
            'qualifications/<int:qualification_id>/edit/']),
        qualification_wizard,
        name='edit-qualification'),
    path(
        '/'.join([
            'providers/<int:provider_id>',
            'campus/<int:campus_id>',
            'qualifications/<int:qualification_id>/']),
        views.show_qualification,
        name='show-qualification'),
    path(
        'sfos/<int:fos_id>/index/',
        sub_field_of_study.index,
        name='list-sfos'),
    path(
        'occupations/',
        occupations.index,
        name='list-occupations'),

    url(r'^test_widgets/$', views.widget_examples, name='test_widgets'),
    url(
        r'^accounts/login/$',
        auth_views.LoginView.as_view(authentication_form=CustomAuthForm),
        name='login'),
    url(
        r'^logout/$',
        auth_views.LogoutView.as_view(), {'next_page': '/'},
        name='logout'),
    url(
        r'user_mgmt/$',
        user_management.show,
        name='show-usermgmt'),
    path(
        r'user_mgmt/add/',
        user_management.add,
        name='add-usermgmt'),
    path(
        r'user_mgmt/edit/<int:user_id>/',
        user_management.edit,
        name='edit-usermgmt'),
    path(
        r'user_mgmt/disabled/<int:user_id>/',
        user_management.disable,
        name='disable-usermgmt'),
    path(
        r'user_mgmt/enabled/<int:user_id>/',
        user_management.enable,
        name='enable-usermgmt'),
    path(
        r'user_mgmt/update/<int:user_id>/',
        user_management.update,
        name='update-usermgmt'),
    path(
        r'user_mgmt/remove/<int:user_id>/',
        # r'user_mgmt/<int:user_id>/remove/$',
        user_management.destroy,
        name='remove-usermgmt'),
    url(
        r'^activate/'
        r'(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user_management.activate,
        # PasswordResetConfirmView.as_view(),
        name='activate'),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        user_management.password_reset,
        name='active_then_set_password'),
    url(
        r'^reset/done/',
        user_management.password_reset__done,
        name='active_then_set_password_done'),
]
