from django.urls import path
from .views import AboutPageView
from . import views
from django.views.i18n import set_language



urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.send_contact_email, name='success'),
    path('about/', AboutPageView.as_view(), name="about"),
    path('i18n/set_language/', set_language, name="set_language"),
]