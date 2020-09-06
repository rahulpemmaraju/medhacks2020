from django.shortcuts import render
from maps.get_covid_data import clean_data,read_all_data
from maps.interactsir1 import determine_cases
import numpy as np

# Create your views here.
def index(request):
    pops,cases,deaths=clean_data()
    total_cases=read_all_data()
    case_std=np.std(total_cases)
    case_mean=np.mean(total_cases)
    context={
        'Title':'COVID-19 Predictive Tracking',
        'Populations':pops.tolist(),
        'Cases':total_cases, 
        'Deaths':deaths.tolist(),
        'STD':case_std,
        'Mean':case_mean, 
    }
    return render(request, 'frontend/index.html',context)
