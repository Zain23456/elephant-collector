from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Elephant, Toy
from .forms import FeedingForm

class ElephantCreate(CreateView):
  model = Elephant
  fields = '__all__'
  # fields = ['name', 'description']
  success_url = '/elephants/'

class ElephantUpdate(UpdateView):
  model = Elephant
  fields = ['description']

class ElephantDelete(DeleteView):
  model = Elephant
  success_url = '/elephants/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def elephants_index(request):
  elephants = Elephant.objects.all()
  return render(request, 'elephants/index.html', { 'elephants': elephants })

def elephants_detail(request, elephant_id):
  elephant = Elephant.objects.get(id=elephant_id)
  feeding_form = FeedingForm()
  return render(request, 'elephants/detail.html', { 'elephant': elephant, 'feeding_form': feeding_form })

def add_feeding(request, elephant_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.elephant_id = elephant_id
    new_feeding.save()
  return redirect('elephants_detail', elephant_id=elephant_id)