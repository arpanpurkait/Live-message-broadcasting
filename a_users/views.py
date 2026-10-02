from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def profile_view(request, username=None):
    profile = request.user.profile 
    return render(request, 'a_users/profile.html', {'profile':profile})



@login_required
def profile_edit_view(request):
    
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
       
        form = ProfileForm(instance=profile)
    return render(request, 'a_users/profile_edit.html', {'form': form, 'profile': profile})