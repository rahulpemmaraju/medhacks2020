from .models import County
from .serializers import CountySerializer
from rest_framework import generics

# Create your views here.
class CountyListCreate(generics.ListCreateAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer