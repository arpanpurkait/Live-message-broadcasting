from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile

# Create your views here.

def profile_view(request, username=None):
    profile = request.user.profile 
    return render(request, 'a_users/profile.html', {'profile':profile})