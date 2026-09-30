from django.shortcuts import render
from .models import Profile

# Create your views here.

def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Now you can safely pass it to your template
    return render(request, 'a_users/profile.html', {'profile': profile})