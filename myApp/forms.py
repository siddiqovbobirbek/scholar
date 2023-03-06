from django import forms
from myApp.models import (
    Bookbaza, Dgubaza, Dissertationbaza, 
    Maqolabaza, Article, Book, Dissertation,
    Certificate
)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'maq_name',
            'maq_muallif',
            'journal_name',
            'maq_nashr_sanasi',
            'bob',
            'number',
            'sahifalar',
        ]

    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'book_muallif',
            'book_nashr_sanasi',
            'nashriyot_name',
        ]


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = [
            'cer_name',
            'cer_muallif',
            'date',
            'dgunomer'
        ]


class DissertationForm(forms.ModelForm):
    class Meta:
        model = Dissertation
        fields = [
            'dis_name',
            'dis_muallif',
            'yunalish'
        ]


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
