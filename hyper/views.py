from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MettoSerializers,iPhoneSerializers
from .models import Metto,iPhone

# Create your views here.

class MettoViewSet(ModelViewSet):
    queryset = Metto.objects.all()
    serializer_class = MettoSerializers


class iPhoneViewSet(ModelViewSet):
    queryset = iPhone.objects.all()
    serializer_class = iPhoneSerializers