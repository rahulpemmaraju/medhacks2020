from django.shortcuts import render
from maps.models import County
# Create your views here.
def index(request):
    context={
        'Title':'COVID-19 Predictive Tracking'
    }
    return render(request, 'frontend/index.html',context)
