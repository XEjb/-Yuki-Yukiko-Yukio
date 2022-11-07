from django.urls import path
from yukiko.views import *

urlpatterns = [
    path('', index),
    path('cats/', categories)
]