from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Url
from .serializers import UrlSerializer

import random

# Create your views here.
@api_view(['POST'])
def shortener(request):
    try:
        url = Url.objects.get(link = request.data["link"])
        serializer = UrlSerializer(url)
        return Response(serializer.data)
    except:
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            temp_url = convert()
            new_link = settings.SITE_URL + temp_url
            serializer.save(new_link = new_link)
            return Response(serializer.data)

def convert():
    encoding = ['0', '1', '2', '3', '4', '5', '6', 
                '7', '8', '9', 'A', 'B', 'C', 'D', 
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                'Z', 'a', 'b', 'c', 'd', 'e', 'f', 
                'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        new_url = ''.join(random.sample(encoding,8))
        try:
            url = Url.objects.get(new_link = new_url)
        except:
            return new_url

def original(request, new_url):
    new_link = settings.SITE_URL + new_url
    url = Url.objects.get(new_link=new_link)
    return HttpResponseRedirect(url.link)