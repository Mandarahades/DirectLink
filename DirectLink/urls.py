from django.contrib.auth import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('forgotten/', index2, name="forgot"),
    path('', index, name="index"),
    path('w/', index3, name="secureSign"),
    path('r/', index4, name="reload"),
    path('admin/', admin.admin.site.urls, name='admin'), #MOT DE PASSE 12345678 NOM MBO

]
