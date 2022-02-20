from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from .models import*

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'full data':'/alldata/',
        'Add movie':'/addview/',

        'seacrh movie by mid': '/searchview_by_mid/<str:pk>/',
        'seacrh movie by rel_year': '/searchview_by_realse_year/<str:pk>/',
        'seacrh movie by Genere': '/searchview_by_Genere/<str:pk>/',


        # 'search data': '/filter1/'
    }
    return Response(api_urls)
    
@api_view(['GET']) 
def alldata(request):
    moviedata=Movie.objects.all()
    serieslmovie=MovieSerializer( moviedata, many=True)
    return Response(serieslmovie.data)

@api_view(['POST'])    
def addview(request):    
    # moviedata = Movie.objects.get(id=pk)
    serieslmovie=MovieSerializer(data=request.data)
    if serieslmovie .is_valid():
        serieslmovie.save()
    return Response(serieslmovie.data)


@api_view(['GET'])    
def searchview_by_mid(request,pk):    
    moviedata = Movie.objects.filter(mid=pk)
    serieslmovie=MovieSerializer( moviedata, many=True)
    return Response(serieslmovie.data)

@api_view(['GET'])    
def searchview_by_realse_year(request,pk):    
    moviedata = Movie.objects.filter(mrelease=pk)
    serieslmovie=MovieSerializer( moviedata, many=True)
    return Response(serieslmovie.data)

@api_view(['GET'])    
def searchview_by_Genere(request,pk):    
    moviedata = Movie.objects.filter(mgeneres=pk)
    serieslmovie=MovieSerializer( moviedata, many=True)
    return Response(serieslmovie.data)

