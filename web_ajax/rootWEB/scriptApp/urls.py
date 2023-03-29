from django.urls import path
from scriptApp import views
from django.http import JsonResponse

urlpatterns=[
    path('main/', views.index),
    path('basic/', views.basic),
    path('dom/', views.dom),
    path('ajax/', views.ajax),
    path('maker/', views.maker)

]