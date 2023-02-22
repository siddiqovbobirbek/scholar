from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from myApp.models import FileHandler, Dgubaza, Dissertationbaza, Maqolabaza, Bookbaza
from .forms import FileHandlerForm, DgubazaForm, DissertationbazaForm, MaqolabazaForm, BookbazaForm
from Users.models import CustomUser
# from django.views import generic
# from django.urls import reverse_lazy
# from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from .models import (
    Certificate, 
    Article,
    Book,
    Dissertation
)

def home(request):
    get_files = FileHandler.objects.prefetch_related('user').all()
    dgu_files = Dgubaza.objects.prefetch_related('user').all()
    book_files = Bookbaza.objects.prefetch_related('user').all()
    maqola_files = Maqolabaza.objects.prefetch_related('user').all()
    disser_files = Dissertationbaza.objects.prefetch_related('user').all()
    print("Files", get_files)
    print("User", request.user)
    context = {
        'get_files':get_files,
        'dgu_files':dgu_files,
        'book_files':book_files,
        'maqola_files':maqola_files,
        'disser_files':disser_files,
        'user': request.user if request.user.is_authenticated else None
        }
    return render(request, "home.html", context)

class IndexView(TemplateView): 
    template_name = "upload.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        get_files = FileHandler.objects.prefetch_related('user').all()
        print("Files", get_files)
        context = {'form':FileHandlerForm, 'get_files':get_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = FileHandlerForm(request.POST, request.FILES, user=request.user)      
            if form.is_valid():
                FileHandler.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))
                return redirect('myApp:upload')
            else:
                context['form'] = form
        else:
            context['form'] = form
        return redirect('myApp:home')

class DGUView(TemplateView): 
    template_name = "upload_dgu.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = Dgubaza.objects.all()
        print("Files", get_files)
        context = {'form':DgubazaForm, 'get_files':get_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = DgubazaForm(request.POST, request.FILES, user=request.user)    
            if form.is_valid():
                Dgubaza.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))

                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            form = DgubazaForm(user = request.user)
            context['form'] = form
        return redirect('myApp:home')

class DissertationView(TemplateView): 
    template_name = "upload_disser.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = Dissertationbaza.objects.all()
        print("Files", get_files)
        context = {'form':DissertationbazaForm, 'get_files':get_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = DissertationbazaForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                Dissertationbaza.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            context['form'] = form
            form = DissertationbazaForm(user = request.user)
        return redirect('myApp:home')



class BookView(TemplateView): 
    template_name = "upload_book.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = Bookbaza.objects.all()
        print("Files", get_files)
        context = {'form':BookbazaForm, 'get_files':get_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = BookbazaForm(request.POST, request.FILES, user=request.user) 
            if form.is_valid():
                Bookbaza.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            form = BookbazaForm(user = request.user)
            context['form'] = form
        return redirect('myApp:home')



class MaqolaView(TemplateView): 
    template_name = "upload_maqola.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = Maqolabaza.objects.all()
        print("Files", get_files)
        context = {'form':MaqolabazaForm, 'get_files':get_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = MaqolabazaForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                Maqolabaza.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            form = MaqolabazaForm(user = request.user)
            context['form'] = form
        return redirect('myApp:home')


        
def show_files(request):
        get_files = FileHandler.objects.prefetch_related('user').last()
        first_file_user = get_files.first()
        print("First", first_file_user.user)
        print("Files", get_files)
        context = {'get_files':get_files}
        return render(request, "files.html", context)


def editor(request):
    context = {}
    return render(request, "editor.html", context)


def book(request):
    user = request.user
    book = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            name = request.POST['name']
            muallif = request.POST['muallif']
            nashr_sanasi = request.POST['nashr_sanasi']
            nashriyot_name = request.POST['nashriyot_name']
            book = Book.objects.create(
                name=name, muallif=muallif, 
                nashriyot_name=nashriyot_name, nashr_sanasi=nashr_sanasi
            )
            print("Kitob: ", book)
        return redirect('myApp:upload_book')    

    context = {
        'book':book
    }
    return render(request, "book.html", context)


def dgu(request):

    user = request.user
    certificate = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            name = request.POST['name']
            muallif = request.POST['muallif']
            date = request.POST['date']
            dgunomer = request.POST['dgunomer']
            certificate = Certificate.objects.create(
                name=name, muallif=muallif, 
                date=date, dgunomer=dgunomer
            )
            print("Sertifikat: ", certificate)
        return redirect('myApp:upload_dgu')    
        
    context = {
        'certificate': certificate
    }
    return render(request, "dgu.html", context)


def dissertation(request):
    user = request.user
    dissertation = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            name = request.POST['name']
            muallif = request.POST['muallif']
            yunalish = request.POST['yunalish']
            dissertation = Dissertation.objects.create(
                name=name, muallif=muallif, 
                yunalish=yunalish
            )
            print("Dissertation: ", dissertation)
        return redirect('myApp:upload_disser')

    context = {
        'dissertation': dissertation
    }
    return render(request, "dissertatsiya.html", context)


def maqola(request):
    user = request.user
    maqola = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            name = request.POST['name']
            muallif = request.POST['muallif']
            journal_name = request.POST['journal_name']
            nashr_sanasi = request.POST['nashr_sanasi']
            bob = request.POST['bob']
            number = request.POST['number']
            sahifalar = request.POST['sahifalar']
            maqola = Article.objects.create(
                name=name, muallif=muallif, 
                journal_name=journal_name, nashr_sanasi=nashr_sanasi,
                bob=bob, number=number, sahifalar=sahifalar
            )
            print("Maqola: ", maqola)
        return redirect('myApp:upload_maqola')
        
    context = {
        'maqola': maqola
    }
    return render(request, "maqola.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def index(request):
    context = {}
    return render(request, "index.html", context)


def search(request):
    query = request.GET.get('query')
    context = {}
    if query:
        certificate = Certificate.objects.filter(name__icontains = query)
        article = Article.objects.filter(name__icontains = query)
        book = Book.objects.filter(name__icontains = query)
        dissertation = Dissertation.objects.filter(name__icontains = query)

        context = {
            "certificate": certificate if certificate.exists() else None,
            "article": article if article.exists() else None,
            "book": book if book.exists() else None,
            "dissertation": dissertation if dissertation.exists() else None
        }
        
    return render(request, "search.html", context)
