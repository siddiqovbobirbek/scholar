from django import forms
from myApp.models import Bookbaza, Dgubaza, Dissertationbaza, Maqolabaza


class BookbazaForm(forms.ModelForm):
    file = forms.FileField
    
    class Meta():
        model = Bookbaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BookbazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        book_baza = super(BookbazaForm, self).save(commit=False)
        book_baza.user = self.user
        if commit:
            book_baza.save()
        return book_baza

class DgubazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Dgubaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DgubazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        dgu_baza = super(DgubazaForm, self).save(commit=False)
        dgu_baza.user = self.user
        if commit:
            dgu_baza.save()
        return dgu_baza



class DissertationbazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Dissertationbaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DissertationbazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        disser_baza = super(DissertationbazaForm, self).save(commit=False)
        disser_baza.user = self.user
        if commit:
            disser_baza.save()
        return disser_baza


class MaqolabazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Maqolabaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MaqolabazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        maqola_baza = super(MaqolabazaForm, self).save(commit=False)
        maqola_baza.user = self.user
        if commit:
            maqola_baza.save()
        return maqola_baza
