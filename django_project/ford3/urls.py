from django.conf.urls import include, url
from ford3.views import views

urlpatterns = [
    url(r'^ProviderForm/', views.provider_form, name='provider_form'),
    url(r'^Widgets/', views.test_widgets, name='test_widgets')

]
