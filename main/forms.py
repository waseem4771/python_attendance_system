from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LeaveRequest, ProfilePicture

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['reason', 'start_date', 'end_date']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ['picture']
