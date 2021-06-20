from django.urls import path, include
from .views import UserProfile
app_name = 'core'

urlpatterns = [
    path('', UserProfile.as_view(), name='home'),
]