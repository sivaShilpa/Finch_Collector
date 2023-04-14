from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
# Create your views here.
# finches = [
#     {'name': 'Mynah', 'breed': 'European goldfinch', 'age': 2},
#     {'name': 'April', 'breed': 'House finch', 'age': 3},
#     {'name': 'Daisy', 'breed': 'Common chaffinch', 'age': 1},
#     {'name': 'Blossom', 'breed': 'American goldfinch', 'age': 4},
#     {'name': 'Cookie', 'breed': 'Eurasian bullfinch', 'age': 5}    
# ]

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'
