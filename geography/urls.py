from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='geography_home'),

    path('areas/', views.AreaList.as_view(), name='arealist'),
    path('attractions/', views.AttractionList.as_view(), name='attractionlist'),

    path('area/create/', views.AreaCreate.as_view(), name='areacreate'),
    path('area/<int:pk>/', views.AreaDetail.as_view(), name='areadetail'),
    path('area/update/<int:pk>/', views.AreaUpdate.as_view(), name='areaupdate'),
    path('area/delete/<int:pk>/', views.AreaDelete.as_view(), name='areadelete'),

    path('attraction/create/', views.AttractionCreate.as_view(), name='attractioncreate'),
    path('attraction/<int:pk>/', views.AttractionDetail.as_view(), name='attractiondetail'),
    path('attraction/update/<int:pk>/', views.AttractionUpdate.as_view(), name='attractionupdate'),
    path('attraction/delete/<int:pk>/', views.AttractionDelete.as_view(), name='attractiondelete'),
]