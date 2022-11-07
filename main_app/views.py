from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Elephant
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