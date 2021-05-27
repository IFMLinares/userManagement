from django.urls import path, include
from .views import inicio
app_name = 'core'

urlpatterns = [
    path('', inicio, name='home'),
]