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

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        if 'bot' in username:
            raise forms.ValidationError("Foydalanuvchi nomida bot so'zi mavjud")
        else:
            return username

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 == password2:
            return self.cleaned_data
        else:
            self.add_error('password1', "Parollar bir biriga teng emas")

    def clean_password1(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if len(password1) < 8:
            msg = "Parol kamida 8 ta belgidan iborat bo'lishi kerak"
            self.add_error('password1', msg)
        return password1

    


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


