from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from User.models import UserProfile
from .forms import ExtendedUserCreationForm, UserProfileForm


def sign_up(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('Index-Page')

    else:
        user_form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'User/SignUp.html', context)


@login_required
def profile(request):
    return render(request, 'User/Profile.html', {'title': 'Profile'})


@login_required
def profile_update(request, id):

    if request.method == 'POST':
        new_email = request.POST.get('user_email')
        new_phone = request.POST.get('user_phone')
        # print(new_email, new_phone)

        user = request.user
        user.email = new_email
        user.save()
        UserProfile.objects.filter(user_id=id).update(user_phone=new_phone)
        return redirect('Profile')

    return render(request, 'User/ProfileUpdate.html', {'title': 'Profile'})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Profile')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'User/Password_Change.html', {'form': form})