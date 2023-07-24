from django.shortcuts import render,  redirect , get_object_or_404, HttpResponse
from .forms import *
from django.contrib import messages
from django.conf import settings
# Create your views here.

def index(request):
    context = {}
    articles = Article.objects.order_by('-id')[0:9]
    context['articles'] = articles
    return render(request, 'website/index.html', context)

def article_details(request, article_slug):
    context = {}
    article = get_object_or_404(Article, slug = article_slug)
    context['article'] = article
    return render(request,'website/article_details.html', context)


def actualite(request):
    context = {}
    try:
        search = request.GET['search']
        print(search)
    except:
        search = None
    if search :
        articles = Article.objects.filter( Titre__contains = search  ).order_by('-id')
    else:
        articles = Article.objects.order_by('-id')
    context['articles'] = articles
    return render(request, 'website/actualite.html', context)


def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/service.html')
    
def organigramme_display(request):
    return render(request, 'website/organigramme.html')

def contacts(request):
    return render(request, 'website/contact.html')

def dashboard(request):
    context = {}

    return render(request,'administration/index.html', context)



def organigramme(request):
    context = {}
    form = GradeForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Enregistrement effectué avec succès')
            return redirect('organigramme')

        else:
            messages.error(request, 'Tout les champ sont requis')
    context['form'] = form
    context['grade'] = Grade.objects.all()
    context['responsable'] = Responsable.objects.all()
    return render(request, 'administration/organigramme/index.html', context)


def responsable_create(request):
    if request.method == 'POST':
        form = ResponsableForm(request.POST or None, request.FILES or None)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('organigramme')
        else:
            print(form.errors)
    else:
        form = ResponsableForm()
    return render(request, 'administration/organigramme/addmembers.html', {'form': form})

def responsable_update(request, pk):
    responsable = get_object_or_404(Responsable, pk=pk)
    if request.method == 'POST':
        form = ResponsableForm(request.POST, request.FILES, instance=responsable)
        if form.is_valid():
            form.save()
            return redirect('organigramme')
    else:
        form = ResponsableForm(instance=responsable)
    return render(request, 'responsable_update.html', {'form': form, 'responsable': responsable})



def responsable_delete(request, pk):
    responsable = get_object_or_404(Responsable, pk=pk)
    if request.method == 'POST':
        responsable.delete()
        return redirect('organigramme')
    return render(request, 'responsable_delete.html', {'responsable': responsable})



def article_list(request):
    return render(request, 'administration/articles/list.html', {'form': form})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('article_create')
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    return render(request, 'administration/articles/create.html', {'form': form})


def Manuel_de_procédures(request):

    file_url = settings.STATIC_URL + 'website/pdf/Draft 1 manuel de procedures CSU1 14.04.2023.pdf'
    context = {'file_url': file_url}
 
    return render(request, 'website/manuel.html', context)


# def download_pdf(request):
#     # Get the file path
#     file_url = settings.STATIC_URL + 'website/pdf/Draft 1 manuel de procedures CSU1 14.04.2023.pdf'
    
#     # Open the file in binary mode
#     with open(file_url, 'rb') as pdf:
#         response = HttpResponse(FileWrapper(pdf), content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment;filename=some_file.pdf'
        
#     return response


from django.http import FileResponse
import os

def download_pdf(request):
    # Get the file path
    file_path = os.path.join(os.path.join(os.path.abspath(__file__)), 'static/website/pdf/Draft 1 manuel de procedures CSU1 14.04.2023.pdf')
    
    # Open the file in binary mode
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=some_file.pdf'
        
    return response