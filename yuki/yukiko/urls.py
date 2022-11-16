from django.urls import path, re_path
from yukiko.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about')
]