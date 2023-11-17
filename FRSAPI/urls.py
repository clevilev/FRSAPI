from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='FRS API Documentation')

urlpatterns = [
    path('api/', include('base.urls')),
    path('', schema_view)
]
