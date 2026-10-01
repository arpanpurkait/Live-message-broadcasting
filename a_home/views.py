from django.shortcuts import render
from a_users.models import Profile

def home_view(request):
    profile = None
    if request.user.is_authenticated:
        profile = request.user.profile  # or Profile.objects.get(user=request.user)
    
    return render(request, 'home.html', {'profile': profile})