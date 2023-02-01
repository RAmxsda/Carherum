from django.shortcuts import render
from .models import *
from Cars.models import  *

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date').all()
    # search_fields = Car.objects.values('model','city','year','body_style')
    model_search = Car.objects.values_list('model',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()

    data = { 
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields':search_fields,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
        'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = { 
        'teams': teams,
     }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')



def contacts(request):
    return render(request,'pages/contacts.html')