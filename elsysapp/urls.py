from django.contrib import admin # pylint: disable=unused-import
from django.urls import path
from .views import index #Relativ import av viewsfunksjonen
from .views import bomstasjon
appname = "elsysapp"
urlpatterns = [
    path('', index, name='index'),
    path("bomstasjon/", bomstasjon, name="bomstasjon")
   # path("chart/", chart, name="chart")
]