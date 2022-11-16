from django.urls import path, re_path
from yukiko.views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:yukio>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]