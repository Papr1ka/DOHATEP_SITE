from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cdo_ska/index.html')

def home(request):
    return render(request, 'cdo_ska/home.html')

def create_test(request):
    return render(request, 'cdo_ska/create_test.html')