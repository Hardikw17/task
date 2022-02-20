from django.urls import path
from . import views

urlpatterns=[

    # path('',views.indexPage,name='index'),
    path('', views.apiOverview, name='api-Overview'),
    path('alldata',views.alldata,name='alldata'),
    path('addview',views.addview,name='addview'),
    path('searchview_by_mid/<str:pk>/', views.searchview_by_mid, name='searchview_by_mid'),
    path('searchview_by_realse_year/<str:pk>/', views.searchview_by_realse_year, name='searchview_by_realse_year'),
    path('searchview_by_Genere/<str:pk>/', views.searchview_by_Genere, name='searchview_by_Genere'),


]