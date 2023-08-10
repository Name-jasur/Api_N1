# import requests
from .serializers import CarSerializers
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Car
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK


@api_view(['GET'])
def AllCar(request,format=None):
    obj = Car.objects.all()
    serializer = CarSerializers(data=obj, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET','PUT','PATCH','DELETE','POST'])
def DetailCar(request, pk):
    def get_queryset(self):
        val = self.queryset
        val.update({'length': len(val['model'])})
        return self.queryset
    if request.method == 'GET':
        obj = Car.objects.get(pk=pk)
        val =CarSerializers(obj).data
        val.update({'len':len(val['model'])})
        ser = CarSerializers(obj)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        obj=Car.objects.get(pk=pk)
        ser=CarSerializers(instance=obj,data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        obj=Car.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/api')
    elif request.method=='POST':
        ser = CarSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)


class GetAllViewset(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

@api_view(['GET'])
def getPersonInfo(request):
    info = {'person':'info'}
    d = dict(request.GET)
    for k in d:
        d[k] = d[k][0]
    info.update(d)
    return Response(info)

def URLShortenerPage(request):
    val = request.POST.get('input_val',None)
    if val:
        url = "https://url-shortener-service.p.rapidapi.com/shorten"

        payload = {"url": val}
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "15b8faf181msh9248a67282a7ff3p1d33e9jsn2576e85b5964",
            "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
        }
        response = requests.post(url, data=payload, headers=headers)
        response = response.json().get('result_url')
    else:
        response = None
    return render(request, 'shortener.html',{'result':response})



