from django.shortcuts import get_object_or_404, render, redirect, Http404, HttpResponseRedirect
from django.urls import reverse
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
        dgu_files = Dgubaza.objects.all()
        print("Files", dgu_files)
        context = {'form':DgubazaForm, 'dgu_files':dgu_files}
        return context

    def post(self, request, **kwargs):
        dgu_name = get_object_or_404(Certificate, pk=kwargs.get('certificate_id'))
        if not dgu_name:
            print("Maqola topilmadi")
            raise Http404("Maqola topilmadi")
        context = {}
        if request.method == 'POST':
            form = DgubazaForm(request.POST, request.FILES, dgu_name = dgu_name)    
            if form.is_valid():
                form.save()
                redirect_url = reverse("myApp:cer_detail", args=[dgu_name.pk])
                return HttpResponseRedirect(redirect_url)
            else:
                context['form'] = form
        else:
            form = DgubazaForm(dgu_name = request.dgu_name)
            context['form'] = form
        return redirect("myApp:home")



class DissertationView(TemplateView): 
    template_name = "upload_disser.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        disser_files = Dissertationbaza.objects.all()
        print("Files", disser_files)
        context = {'form':DissertationbazaForm, 'disser_files':disser_files}
        return context

    def post(self, request, **kwargs): 
        disser_name = get_object_or_404(Dissertation, pk=kwargs.get('dissertation_id'))
        context = {}
        if request.method == 'POST':
            form = DissertationbazaForm(request.POST, request.FILES, disser_name = disser_name)
            if form.is_valid():
                form.save()
                redirect_url = reverse("myApp:diss_detail", args=[disser_name.pk])
                return HttpResponseRedirect(redirect_url)
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
        book_files = Bookbaza.objects.all()
        print("Files", book_files)
        context = {'form':BookbazaForm, 'book_files':book_files}
        return context

    def post(self, request, **kwargs): 
        kitob_name = get_object_or_404(Book, pk=kwargs.get('book_id'))
        context = {}
        if request.method == 'POST':
            form = BookbazaForm(request.POST, request.FILES, kitob_name = kitob_name) 
            if form.is_valid():
                form.save()
                redirect_url = reverse("myApp:book_detail", args=[kitob_name.pk])
                return HttpResponseRedirect(redirect_url)
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
        context = {'form':MaqolabazaForm, 'maqola_files':maqola_files}
        return context

    def post(self, request, **kwargs): 
        maqola_name = get_object_or_404(Article, pk=kwargs.get('maqola_id'))
        context = {}
        if request.method == 'POST':
            form = MaqolabazaForm(request.POST, request.FILES, maqola_name = maqola_name)
            if form.is_valid():
                form.save()
                redirect_url = reverse("myApp:artic_detail", args=[maqola_name.pk])
                return HttpResponseRedirect(redirect_url)
            else:
                context['form'] = form
        else:
            form = MaqolabazaForm(maqola_name = request.maqola_name)
            context['form'] = form
        return redirect('myApp:home')




def editor(request):
    context = {}
    return render(request, "editor.html", context)


@login_required
def book(request):
    user = request.user
    book = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            book_name = request.POST['book_name']
            book_muallif = request.POST['book_muallif']
            book_nashr_sanasi = request.POST['book_nashr_sanasi']
            volume = request.POST['volume']
            pages = request.POST['pages']
            book = Book.objects.create(
                book_name=book_name, book_muallif=book_muallif, 
                pages=pages, book_nashr_sanasi=book_nashr_sanasi, volume=volume
            )
            print("Kitob: ", book)
            url = reverse('myApp:upload_book', kwargs={'book_id': book.pk} )
        return redirect(url)      

    context = {
        'book':book
    }
    return render(request, "book.html", context)


@login_required
def dgu(request):
    user = request.user
    certificate = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            cer_name = request.POST['cer_name']
            cer_muallif = request.POST['cer_muallif']
            date = request.POST['date']
            dgunomer = request.POST['dgunomer']
            application_number = request.POST['application_number']
            certificate = Certificate.objects.create(
                cer_name=cer_name, cer_muallif=cer_muallif, 
                date=date, dgunomer=dgunomer, application_number=application_number
            )
            print("Sertifikat: ", certificate)
            url = reverse('myApp:upload_dgu', kwargs={'certificate_id': certificate.pk} )
        return redirect(url)    
        
    context = {
        'certificate': certificate
    }
    return render(request, "dgu.html", context)


@login_required
def dissertation(request):
    user = request.user
    dissertation = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            dis_name = request.POST['dis_name']
            dis_muallif = request.POST['dis_muallif']
            dis_nashr_sanasi = request.POST['dis_nashr_sanasi']
            institut = request.POST['institut']
            dissertation = Dissertation.objects.create(
                dis_name=dis_name, dis_muallif=dis_muallif, 
                dis_nashr_sanasi=dis_nashr_sanasi, institut=institut
            )
            print("Dissertation: ", dissertation)
            url = reverse('myApp:upload_disser', kwargs={'dissertation_id': dissertation.pk} )
        return redirect(url) 

    context = {
        'dissertation': dissertation
    }
    return render(request, "dissertatsiya.html", context)


@login_required
def maqola(request):
    user = request.user
    maqola = None
    if request.method == 'POST':
        if user is not None and user.is_authenticated:
            maq_name = request.POST['maq_name']
            maq_muallif = request.POST['maq_muallif']
            journal_name = request.POST['journal_name']
            maq_nashr_sanasi = request.POST['maq_nashr_sanasi']
            volum = request.POST['volum']
            issue = request.POST['issue']
            sahifalar = request.POST['sahifalar']
            maqola = Article.objects.create(
                maq_name=maq_name, maq_muallif=maq_muallif, 
                journal_name=journal_name, maq_nashr_sanasi=maq_nashr_sanasi,
                volum=volum, issue=issue, sahifalar=sahifalar
            )
            print("Maqola: ", maqola)
            url = reverse('myApp:upload_maqola', kwargs={'maqola_id': maqola.pk} )
        return redirect(url) 
        
    context = {
        'maqola': maqola
    }
    return render(request, "maqola.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


@login_required
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




def book_detail(request, pk):
    book = None
    try:
        book = Book.objects.get(pk=pk)

    except Book.DoesNotExist:
        raise Http404("Bunday kitob mavjud emas")
    
    book_files = Bookbaza.objects.filter(kitob_name=book).prefetch_related('kitob_name').all()
        
    context = {
        'book': book,
        'book_files': book_files,
        'muallif': book.book_muallif.replace(',', ';', '\n'),
        'mualliflar': book.book_muallif.split(',')
        
    }   
    
    return render(request, "book_detail.html", context)




def cer_detail(request, pk):
    try:
        certificate = Certificate.objects.get(pk=pk)

    except Certificate.DoesNotExist:
        raise Http404("Bunday dasturiy guvohnoma mavjud emas")
    
    dgu_files = Dgubaza.objects.filter(dgu_name=certificate).prefetch_related('dgu_name').all()
    # print("User", request.POST.get('dgu_name'))
    
    context = {
        'certificate': certificate,
        'dgu_files':dgu_files,
        'cer_muallif': certificate.cer_muallif.replace(',', ';', '\n'),
        'cer_mualliflar': certificate.cer_muallif.split(',')
    }
    
    return render(request, "cer_detail.html", context)




def artic_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        raise Http404("Bunday maqola mavjud emas")
    
    maqola_files = Maqolabaza.objects.filter(maqola_name=article).prefetch_related('maqola_name').all()
    
    context = {
        'article': article,
        'maqola_files': maqola_files,
        'maq_muallif': article.maq_muallif.replace(',', ';', '\n'),
        'maq_mualliflar': article.maq_muallif.split(','),
        'volum': article.volum,
        'issue': article.issue,
        'journal_name': article.journal_name,
        'maq_sahifa': article.sahifalar.split('-'),
    }
    
    return render(request, "maq_detail.html", context)




def diss_detail(request, pk):
    try:
        dissertation = Dissertation.objects.get(pk=pk)

    except Dissertation.DoesNotExist:
        raise Http404("Bunday dissertatsiya mavjud emas")
    
    disser_files = Dissertationbaza.objects.filter(disser_name=dissertation).prefetch_related('disser_name').all()
    
    context = {
        'dissertation': dissertation,
        'disser_files':disser_files,
        'dis_muallif': dissertation.dis_muallif.replace(',', ';', '\n'),
        'dis_mualliflar': dissertation.dis_muallif.split(',')
    }
    
    return render(request, "diss_detail.html", context)
