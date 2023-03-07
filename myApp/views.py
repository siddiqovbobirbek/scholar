from django.shortcuts import render, redirect, Http404
from django.views.generic import TemplateView
from myApp.models import  Dgubaza, Dissertationbaza, Maqolabaza, Bookbaza, FAQ
from .forms import (
    DgubazaForm, DissertationbazaForm, MaqolabazaForm, 
    BookbazaForm, BookForm, ArticleForm, CertificateForm, 
    DissertationForm
)


from django.contrib.auth.decorators import login_required

from .models import (
    Certificate, 
    Article,
    Book,
    Dissertation
)

def home(request):
    context = {
        'user': request.user if request.user.is_authenticated else None
    }
    return render(request, "home.html", context)


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
            form = DgubazaForm(request.POST, request.FILES, dgu_name = request.POST.get('dgu_name'))    
            if form.is_valid():
                form.save()
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            form = DgubazaForm(dgu_name = request.dgu_name)
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
            form = DissertationbazaForm(request.POST, request.FILES, disser_name = request.POST.get('disser_name'))
            if form.is_valid():
                form.save()
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            context['form'] = form
            form = DissertationbazaForm(disser_name = request.disser_name)
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
            form = BookbazaForm(request.POST, request.FILES, kitob_name = request.POST.get('kitob_name')) 
            if form.is_valid():
                form.save()
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            form = BookbazaForm(kitob_name = request.kitob_name)
            context['form'] = form
        return redirect('myApp:home')



class MaqolaView(TemplateView): 
    template_name = "upload_maqola.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maqola_files = Maqolabaza.objects.all()
        print("Files", maqola_files)
        context = {'form':MaqolabazaForm, 'get_files':maqola_files}
        return context

    def post(self, request, **kwargs): 
        context = {}
        if request.method == 'POST':
            form = MaqolabazaForm(request.POST, request.FILES, maqola_name = request.POST.get('maqola_name'))
            if form.is_valid():
                form.save()
                return redirect('myApp:home')
            else:
                context['form'] = form
        else:
            form = MaqolabazaForm(maqola_name = request.maqola_name)
            context['form'] = form
        return redirect('myApp:home')


        
# def show_files(request):
#         get_files = FileHandler.objects.prefetch_related('user').last()
#         first_file_user = get_files.first()
#         print("First", first_file_user.user)
#         print("Files", get_files)
#         context = {'get_files':get_files}
#         return render(request, "files.html", context)


def editor(request):
    context = {}
    return render(request, "editor.html", context)


def book(request):
    user = request.user
    book = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            book_name = request.POST['book_name']
            book_muallif = request.POST['book_muallif']
            book_nashr_sanasi = request.POST['book_nashr_sanasi']
            nashriyot_name = request.POST['nashriyot_name']
            book = Book.objects.create(
                book_name=book_name, book_muallif=book_muallif, 
                nashriyot_name=nashriyot_name, book_nashr_sanasi=book_nashr_sanasi
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
            cer_name = request.POST['cer_name']
            cer_muallif = request.POST['cer_muallif']
            date = request.POST['date']
            dgunomer = request.POST['dgunomer']
            certificate = Certificate.objects.create(
                cer_name=cer_name, cer_muallif=cer_muallif, 
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
            dis_name = request.POST['dis_name']
            dis_muallif = request.POST['dis_muallif']
            yunalish = request.POST['yunalish']
            dissertation = Dissertation.objects.create(
                dis_name=dis_name, dis_muallif=dis_muallif, 
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
            maq_name = request.POST['maq_name']
            maq_muallif = request.POST['maq_muallif']
            journal_name = request.POST['journal_name']
            maq_nashr_sanasi = request.POST['maq_nashr_sanasi']
            bob = request.POST['bob']
            number = request.POST['number']
            sahifalar = request.POST['sahifalar']
            maqola = Article.objects.create(
                maq_name=maq_name, maq_muallif=maq_muallif, 
                journal_name=journal_name, maq_nashr_sanasi=maq_nashr_sanasi,
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



def faq_view(request):
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")
    context = {
        'faq': faq
    }
    return render(request, "faq.html", context)




def book_detail(request, book_id):
    book = None
    try:
        book = Book.objects.get(pk=book_id)

    except Book.DoesNotExist:
        raise Http404("Bunday kitob mavjud emas")
    
    book_files = Bookbaza.objects.prefetch_related('user').all()
    print("Book", request.POST.get('book_name'))
    
    context = {
        'book': book,
        'book_files': book_files,
        'muallif': book.book_muallif.replace(',', '\n'),
        'mualliflar': book.book_muallif.split(',')
        
    }   
    
    return render(request, "book_detail.html", context)




def cer_detail(request, dgu_id):
    try:
        certificate = Certificate.objects.get(pk=dgu_id)

    except Certificate.DoesNotExist:
        raise Http404("Bunday dasturiy guvohnoma mavjud emas")
    
    dgu_files = Dgubaza.objects.prefetch_related('user').all()
    print("User", request.POST.get('dgu_name'))
    
    context = {
        'certificate': certificate,
        'dgu_files':dgu_files,
        'cer_muallif': certificate.cer_muallif.replace(',', '\n'),
        'cer_mualliflar': certificate.cer_muallif.split(',')
    }
    
    return render(request, "cer_detail.html", context)




def artic_detail(request, artic_id):
    try:
        article = Article.objects.get(pk=artic_id)

    except Article.DoesNotExist:
        raise Http404("Bunday maqola mavjud emas")
    
    maqola_files = Maqolabaza.objects.prefetch_related('maqola_name').all()
    print("Article", request.POST.get('maqola_name'))
    
    context = {
        'article': article,
        'maqola_files': maqola_files,
        'maq_muallif': article.maq_muallif.replace(',', '\n'),
        'maq_mualliflar': article.maq_muallif.split(','),
        'bob': article.bob,
        'number': article.number,
        'journal_name': article.journal_name,
        'maq_sahifa': article.sahifalar.split('-'),
    }
    
    return render(request, "maq_detail.html", context)




def diss_detail(request, diss_id):
    try:
        dissertation = Dissertation.objects.get(pk=diss_id)

    except Dissertation.DoesNotExist:
        raise Http404("Bunday dissertatsiya mavjud emas")
    
    disser_files = Dissertationbaza.objects.prefetch_related('user').all()
    print("User", request.POST.get('disser_name'))
    
    context = {
        'dissertation': dissertation,
        'disser_files':disser_files,
        'dis_muallif': dissertation.dis_muallif.replace(',', '\n'),
        'dis_mualliflar': dissertation.dis_muallif.split(',')
    }
    
    return render(request, "diss_detail.html", context)
