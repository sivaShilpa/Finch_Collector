from django.shortcuts import render

# Create your views here.
finches = [
    {'name': 'Mynah', 'breed': 'European goldfinch', 'age': 2},
    {'name': 'April', 'breed': 'House finch', 'age': 3},
    {'name': 'Daisy', 'breed': 'Common chaffinch', 'age': 1},
    {'name': 'Blossom', 'breed': 'American goldfinch', 'age': 4},
    {'name': 'Cookie', 'breed': 'Eurasian bullfinch', 'age': 5}    
]

def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})