from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
# Create your views here.
def inicio(request):
    return redirect('accounts/login')