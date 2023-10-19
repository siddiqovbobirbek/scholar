import codecs
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
            'volum',
            'issue',
            'sahifalar',
        ]

    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'book_muallif',
            'book_nashr_sanasi',
            'volume',
            'pages'
        ]


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = [
            'cer_name',
            'cer_muallif',
            'date',
            'dgunomer',
            'application_number',
        ]


class DissertationForm(forms.ModelForm):
    class Meta:
        model = Dissertation
        fields = [
            'dis_name',
            'dis_muallif',
            'dis_nashr_sanasi',
            'institut',
        ]


class BookbazaForm(forms.ModelForm):
    file = forms.FileField
    
    class Meta():
        model = Bookbaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.kitob_name = kwargs.pop('kitob_name', None)
        super(BookbazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        book_baza = super(BookbazaForm, self).save(commit=False)
        book_baza.kitob_name = self.kitob_name
        if commit:
            book_baza.save()
        return book_baza

class DgubazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Dgubaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.dgu_name = kwargs.pop('dgu_name', None)
        super(DgubazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        dgu_baza = super(DgubazaForm, self).save(commit=False)
        dgu_baza.dgu_name = self.dgu_name
        if commit:
            dgu_baza.save()
        return dgu_baza



class DissertationbazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Dissertationbaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.disser_name = kwargs.pop('disser_name', None)
        super(DissertationbazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        disser_baza = super(DissertationbazaForm, self).save(commit=False)
        disser_baza.disser_name = self.disser_name
        if commit:
            disser_baza.save()
        return disser_baza


class MaqolabazaForm(forms.ModelForm):
    file = forms.FileField

    class Meta():
        model = Maqolabaza
        fields = ('file_upload',)

    def __init__(self, *args, **kwargs):
        self.maqola_name = kwargs.pop('maqola_name', None)
        super(MaqolabazaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        try:
            maqola_baza = super(MaqolabazaForm, self).save(commit=False)
            maqola_baza.maqola_name = self.maqola_name
            if commit:
                with open(maqola_baza.file_upload.path, 'w', encoding='utf-8') as file:
                    content = maqola_baza.file_upload.read().decode('utf-8')
                    file.write(content)
                maqola_baza.save()
            return maqola_baza
        except Exception as e:
            print(e)
            raise e