from django.shortcuts import render
from maps.get_covid_data import clean_data,read_all_data
from maps.interactsir1 import determine_cases
import numpy as np

# Create your views here.
def index(request):
    pops,cases,deaths=clean_data()
    read_all_data()
    context={
        'Title':'COVID-19 Predictive Tracking',
        'Populations':pops.tolist(),
        'Cases':cases.tolist(), 
        'Deaths':deaths.tolist(), 
    }
    return render(request, 'frontend/index.html',context)
