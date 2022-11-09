from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Elephant, Toy
from .forms import FeedingForm

class ElephantCreate(CreateView):
  model = Elephant
  # fields = '__all__'
  fields = ['name', 'description']
  success_url = '/elephants/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def elephants_index(request):
  elephants = request.user.elephant_set.all()
  return render(request, 'elephants/index.html', { 'elephants': elephants })

def elephants_detail(request, elephant_id):
  elephant = Elephant.objects.get(id=elephant_id)
  toys_elephant_doesnt_have = Toy.objects.exclude(id__in = elephant.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'elephants/detail.html', { 'elephant': elephant, 'feeding_form': feeding_form, 'toys': toys_elephant_doesnt_have })

def add_feeding(request, elephant_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.elephant_id = elephant_id
    new_feeding.save()
  return redirect('elephants_detail', elephant_id=elephant_id)

def assoc_toy(request, elephant_id, toy_id):
  Elephant.objects.get(id=elephant_id).toys.add(toy_id)
  return redirect('elephants_detail', elephant_id=elephant_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('elephants_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)