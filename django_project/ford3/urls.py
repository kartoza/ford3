from django.conf.urls import url
from ford3.views import views

urlpatterns = [
    url(r'^ProviderForm/$', views.provider_form, name='provider_form'),
    url(r'^$', views.widget_examples, name='test_widgets')

]
