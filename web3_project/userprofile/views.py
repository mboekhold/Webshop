from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    user = request.user
    return render(request, 'userprofile/profile.html', {'profile': user.profile})

@login_required
def changeProfile(request):
        user = request.user
        if request.method == 'POST':

            user_form = forms.UserChangeForm(request.POST, instance=user)
            profile_form = forms.ProfileChangeForm(request.POST, request.FILES, instance=user.profile)

            if all((profile_form.is_valid(), user_form.is_valid())):
                user_form.save()
                profile_form.save()
                username = user.username
                messages.success(request, f'Profile was changed for {username}!')
                return redirect('profile')
        else:
            user_form = forms.UserChangeForm(instance=user)
            profile_form = forms.ProfileChangeForm(instance=user.profile)
        return render(request, 'userprofile/change.html', {'profile_form': profile_form, 'user_form': user_form})
