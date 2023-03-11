from django.http import QueryDict
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Test, Profession
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'cdo_ska/index.html')

def is_valid_queryparam(param):
    return param != '' and param is not None

def is_int(param):
    try:
        int(param)
    except:
        return False
    else:
        return True

class HomePageView(ListView):
    model = Test
    template_name = "cdo_ska/home.html"
    paginate_by = 30
    queryset = Test.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #custom context here
        context['professions'] = Profession.objects.all()
        queryset = Test.objects.all()
        context['years'] = [model.year for model in queryset.dates('date', 'year')]
        context['months'] = [model for model in queryset.dates('date', 'month')]
        
        form_data = []
        
        for value in self.request.GET:
            if value.startswith("year") or value.startswith("month") or value.startswith("profession"):
                form_data.append(value)

        context['form_data'] = form_data
        
        test_count = self.queryset.count()
        message = ""
        if test_count % 100 in (11, 12, 13, 14):
            message = "Тестов найдено"
        elif test_count % 10 == 1:
            message = "Тест найден"
        elif test_count % 10 in (2, 3, 4):
            message = "Теста найдено"
        else:
            message = "Тестов найдено"
        
        context['message'] = message
        context['query'] = self.request.GET.get("query", "")
        
        return context
    
    def get(self, request, *args, **kwargs):
        
        if request.GET.get("query"):
            query = request.GET.get("query")
            self.queryset = Test.objects.filter(Q(name__icontains=query) | Q(questions__question__icontains=query) | Q(questions__answer__icontains=query))
            return super().get(request, *args, **kwargs)
        
        query = Q()
        
        for param in request.GET:
            if is_valid_queryparam(param):
                if param.startswith("year_"):
                    year = request.GET.get(param)
                    if is_int(year):
                        query = query | (Q(date__year=int(year)))
                elif param.startswith("month_"):
                    month = request.GET.get(param)
                    if is_int(month):
                        query = query | (Q(date__month=int(month)))
                elif param.startswith("profession_"):
                    profession = request.GET.get(param)
                    if is_int(profession):
                        query = query | (Q(profession__exact=int(profession)))
        
        self.queryset = Test.objects.filter(query)
        
        return super().get(request, *args, **kwargs)
        

def home(request):
    return render(request, 'cdo_ska/home.html')

def create_test(request):
    return render(request, 'cdo_ska/create_test.html')

def test(request):
    return render(request, 'cdo_ska/test.html')
