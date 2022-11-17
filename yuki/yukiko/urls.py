from django.urls import path, re_path
from yukiko.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('addpage/', contact, name='contact'),
    path('addpage/', login, name='login'),
]