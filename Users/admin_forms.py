from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

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
            raise forms.ValidationError("The username contains the word bot")
        else:
            return username

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 == password2:
            return self.cleaned_data
        else:
            self.add_error('password2', "The two password fields didn’t match.")

    def clean_password1(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if len(password1) < 8:
            msg = "Password must be at least 8 characters long"
            self.add_error('password2', msg)
        return password1

    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('first_name', "First name and last name are entered the same")

        else:
            return self.cleaned_data



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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'user', 'first_name', 'last_name', 'address', 'number', 'age', 'job')
