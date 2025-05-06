from django.shortcuts import render
from django.http import JsonResponse
from .serializers import BeveragesSerializers
from .models import Beverages
# Create your views here.


def Beverages_List(request):
    beverages = Beverages.objects.all()
    serializers_class = BeveragesSerializers(beverages,many=True)
    return JsonResponse({'beverages':serializers_class.data})