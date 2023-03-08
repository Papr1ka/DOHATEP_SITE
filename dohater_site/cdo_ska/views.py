from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Test

# Create your views here.
def index(request):
    return render(request, 'cdo_ska/index.html')

class HomePageView(ListView):
    model = Test
    template_name = "cdo_ska/home.html"
    context_object_name = "tests"
    paginate_by = 50
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #custom context here
        
        return context
        

def home(request):
    return render(request, 'cdo_ska/home.html', context)

def create_test(request):
    return render(request, 'cdo_ska/create_test.html')

def test(request):
    return render(request, 'cdo_ska/test.html')