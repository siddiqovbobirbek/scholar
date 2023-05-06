from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .admin_forms import CustomUserCreationForm


class RegisterForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'username',
        })
        self.fields["first_name"].widget.attrs.update({
            'required':'',
            'name':'first_name',
            'id':'first_name',
            'type':'text',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'first name',
        })
        self.fields["last_name"].widget.attrs.update({
            'required':'',
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'last name',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'email',
            'type':'text',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'email',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'id_password1',
            'type':'password',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'password',
            'minleght':'8'
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'id_password2',
            'type':'password',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'password',
            'minleght':'8'
        })
        self.fields["address"].widget.attrs.update({
            'required':'',
            'name':'address',
            'id':'address',
            'type':'address',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'address',
        })
        self.fields["job"].widget.attrs.update({
            'required':'',
            'name':'job',
            'type':'job',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'activity',
        })
        self.fields["age"].widget.attrs.update({
            'required':'',
            'name':'age',
            'type':'age',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'age',
        })
        self.fields["number"].widget.attrs.update({
            'required':'',
            'name':'number',
            'type':'number',
            'style':'font-size:15px',
            'class':'form-control form-control-md',
            'placeholder':'phone number',
        })

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields


    
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'required':'',
            'name':'first_name',
            'style':'font-size:13px',
            'class':'form-control'
        }),
        self.fields["last_name"].widget.attrs.update({
            'required':'',
            'name':'last_name',
            'style':'font-size:13px',
            'class':'form-control'
        }),
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'style':'font-size:13px',
            'class':'form-control'
        }),
        self.fields["job"].widget.attrs.update({
            'required':'',
            'name':'job',
            'style':'font-size:13px',
            'class':'form-control'
        }),
        self.fields["number"].widget.attrs.update({
            'required':'',
            'name':'number',
            'style':'font-size:13px',
            'class':'form-control'
        }),
        self.fields["address"].widget.attrs.update({
                'required':'',
                'name':'address',
                'style':'font-size:13px',
                'class':'form-control'
            }),


    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'job',
            'number',
            'age',
            'address'
        ]


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

#     def clean_username(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         if 'bot' in username:
#             raise forms.ValidationError("Foydalanuvchi ismida bot so'zi mavjud")
#         else:
#             return username

#     def clean_email(self, *args, **kwargs):
#         email = self.cleaned_data.get('email')
#         if 'gmail.com' in email:
#             return email
#         else:
#             raise forms.ValidationError("Foydalanuvchi 'gmail.com' ni kiritmadi")

#     def clean(self, *args, **kwargs):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 == password2:
#             return self.cleaned_data
#         else:
#             self.add_error('password2', "Parollar bir biriga teng emas ")

#     def clean_password1(self, *args, **kwargs):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         x = password1.isalpha()
#         n = password1.isalnum()
#         if len(password1) < 7:
#             msg = "Parol kamida 7 ta belgidan iborat bo'lishi kerak"
#             self.add_error('password2', msg)

#         elif n or x == False:
#             msg = "Parolda kamida 1 raqam bo'lishi kerak."
#             self.add_error('password1', msg)

#         elif password1 != password2:
#             msg = "Parollar bir biriga teng emas. "
#             self.add_error('password2', msg)

#         return password1

#     def clean(self, *args, **kwargs):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')

#         if first_name == last_name:
#             self.add_error('first_name', "Ism familiya bir xil kiritildi")

#         else:
#             return self.cleaned_data

#     def clean_password2(self, *args, **kwargs):
#         password2 = self.cleaned_data.get('password2')

#         if password2 == "qwerty12345" "admin12345":
#             self.add_error('password1', "Bunday parol mavjud")

#         else:
#             return password2
