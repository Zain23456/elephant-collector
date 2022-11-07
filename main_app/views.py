from django.shortcuts import render
from .models import Elephant


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
  return render(request, 'elephants/detail.html', { 'elephant': elephant })