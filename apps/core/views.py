from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404

from .models import User
# Create your views here.

class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'index.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        context = {
            'user': user,
        }
        return render(self.request, self.template_name, context)
