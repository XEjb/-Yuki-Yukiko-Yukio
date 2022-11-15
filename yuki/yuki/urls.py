
from django.contrib import admin
from django.urls import path, include
from yukiko.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yukiko.urls'))
]
