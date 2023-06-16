from django.contrib.auth import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/<uidb64>/<token>/', reset_password_confirm, name='reset_password_confirm'),
    path('admin/', admin.admin.site.urls, name='admin'), #MOT DE PASSE 12345678 NOM MBO

]
