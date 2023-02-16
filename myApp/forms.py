from django import forms
from myApp.models import FileHandler, Bookbaza, Dgubaza, Dissertationbaza, Maqolabaza

class FileHandlerForm(forms.ModelForm):

    file = forms.FileField

    class Meta():
        model = FileHandler
        fields = ('file_upload',)

class BookbazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Bookbaza
        fields = ('file_upload',)

class DgubazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Dgubaza
        fields = ('file_upload',)



class DissertationbazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Dissertationbaza
        fields = ('file_upload',)


class MaqolabazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Maqolabaza
        fields = ('file_upload',)
