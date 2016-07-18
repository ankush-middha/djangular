from django.conf.urls import patterns, url
from login import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url('landing-page/$', TemplateView.as_view(template_name='login.html')),
    url('registration-api/$', views.RegistrationApi.as_view(), name='registration-api'),
    url('login-api/$', views.LoginApi.as_view(), name='login-api'),
    url('profile-api/$', views.ProfileApi.as_view(), name='profile-api'),
    url(r'^profile-image-api/$', views.ProfileImageApi.as_view(), name='profile-image-api'),
)
