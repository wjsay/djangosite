from django.conf.urls import url
from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('moments_input/', views.moments_input, name='moments_input'),
    url(r'', views.welcome, name='welcome'),
]
