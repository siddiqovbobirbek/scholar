from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    address = forms.CharField(max_length=255, required=True)
    number = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    job = forms.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'address', 'number', 'age', 'job')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.address = self.cleaned_data['address']
        user.number = self.cleaned_data['number']
        user.age = self.cleaned_data['age']
        user.job = self.cleaned_data['job']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(max_length=150, required=True)
    address = forms.CharField(max_length=255, required=True)
    number = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    job = forms.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'address', 'number', 'age', 'job')
