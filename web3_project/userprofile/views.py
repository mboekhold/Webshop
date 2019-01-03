from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def changeProfile(request):
    from PIL import Image
    import io
    user = request.user
    if request.method == 'POST':

        user_form = forms.UserChangeForm(request.POST, instance=user)
        profile_form = forms.ProfileChangeForm(request.POST, request.FILES, instance=user.profile)

        if all((profile_form.is_valid(), user_form.is_valid())):
            user_form.save()
            profile_form.save()
            username = user.username
            messages.success(request, f'Profile was changed for {username}!')
            return redirect('shop:profile')
    else:
        user_form = forms.UserChangeForm(instance=user)
        profile_form = forms.ProfileChangeForm(instance=user.profile)
    return render(request, 'accounts/change.html', {'profile_form': profile_form, 'user_form': user_form})
