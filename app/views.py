from django.shortcuts import render,  redirect , get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.

def index(request):
    context = {}
    return render(request, 'website/index.html', context)



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