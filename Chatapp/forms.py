from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2']
    
class CheckoutForm(forms.Form):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True)
    phone_number = forms.CharField(label='Phone Number', required=True)
    address = forms.CharField(label='Address', required=True)

    class Meta:
        model = Profile
        fields = ['email', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email
        self.fields['phone_number'].initial = self.instance.phone_number
        self.fields['address'].initial = self.instance.address

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        user = User.objects.get(id=self.instance.user.id)
        user.email = self.cleaned_data['email']
        user.save()
        profile.phone_number = self.cleaned_data['phone_number']
        profile.address = self.cleaned_data['address']
        profile.save()
        return profile
    

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'profile_picture']