from django.shortcuts import render, redirect
from .forms import CarroForm
from .models import Carro


# Create your views here.
def home(request):
    data = {}
    data['dbs'] = Carro.objects.all()
    return render(request,'index.html', data)

def form(request):
    data = {}
    data['form'] = CarroForm()
    return render(request,'form.html', data)

def create(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['dbs'] = Carro.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['dbs'] = Carro.objects.get(pk=pk)
    data['form'] = CarroForm(instance= data['dbs'])
    return render(request, 'form.html', data)

def update(request,pk):
    data = {}
    data['dbs'] = Carro.objects.get(pk=pk)
    form = CarroForm(request.POST or None, instance=data['dbs'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Carro.objects.get(pk = pk)
    db.delete()
    return redirect('home')
    



