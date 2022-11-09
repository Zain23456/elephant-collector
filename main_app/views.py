from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Elephant, Toy, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'honeybee-cheese-elephant-collector'

class ElephantCreate(CreateView, LoginRequiredMixin):
  model = Elephant
  # fields = '__all__'
  fields = ['name', 'description']
  success_url = '/elephants/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ElephantUpdate(UpdateView, LoginRequiredMixin):
  model = Elephant
  fields = ['description']

class ElephantDelete(DeleteView, LoginRequiredMixin):
  model = Elephant
  success_url = '/elephants/'

class ToyCreate(CreateView, LoginRequiredMixin):
  model = Toy
  fields = '__all__'

class ToyList(ListView, LoginRequiredMixin):
  model = Toy

class ToyDetail(DetailView, LoginRequiredMixin):
  model = Toy

class ToyUpdate(UpdateView, LoginRequiredMixin):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView, LoginRequiredMixin):
  model = Toy
  success_url = '/toys/'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def elephants_index(request):
  elephants = request.user.elephant_set.all()
  return render(request, 'elephants/index.html', { 'elephants': elephants })

@login_required
def elephants_detail(request, elephant_id):
  elephant = Elephant.objects.get(id=elephant_id)
  toys_elephant_doesnt_have = Toy.objects.exclude(id__in = elephant.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'elephants/detail.html', { 'elephant': elephant, 'feeding_form': feeding_form, 'toys': toys_elephant_doesnt_have })

@login_required
def add_feeding(request, elephant_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.elephant_id = elephant_id
    new_feeding.save()
  return redirect('elephants_detail', elephant_id=elephant_id)

@login_required
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

def add_photo(request, elephant_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, elephant_id=elephant_id)
      elephant_photo = Photo.objects.filter(elephant_id=elephant_id)
      if elephant_photo.first():
        elephant_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('cats_detail', elephant_id=elephant_id)