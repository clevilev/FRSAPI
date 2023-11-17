from django.urls import path
from .views import *

urlpatterns = [
    path('call_insert_procedure/', call_insert_procedure, name='call_insert_procedure'),
    path('create_user/', create_user, name='create_user'),
    path('login/', login, name='login'),
    path('get_auth_group/', get_auth_group, name='get_auth_group'),
]
