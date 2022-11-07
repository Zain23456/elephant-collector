from django.shortcuts import render
from django.http import HttpResponse


class Elephant:
  def __init__(self, name, description):
    self.name = name
    self.description = description

elephants = [
  Elephant('Lolo', 'kinda rude'),
  Elephant('Achi', 'Looks majestic'),
  Elephant('Fancy', 'happy')
]
# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def elephants_index(request):
  return render(request, 'elephants/index.html', { 'elephants': elephants })
