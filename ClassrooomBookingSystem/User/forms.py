from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(ExtendedUserCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    user_name = forms.CharField(max_length=30, required=True, help_text='Your Name', label='Full Name',
                                widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    user_identity = forms.IntegerField(required=True, help_text='Staff/Student ID', label='Identity Number')
    user_phone = forms.CharField(required=False, help_text='Phone Number', label='Phone Number',
                                 widget=forms.TextInput(attrs={'placeholder': 'Format : 0XX-XXXXXXX'}))

    class Meta:
        model = UserProfile
        fields = ('user_name', 'user_identity', 'user_phone')

