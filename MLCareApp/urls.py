from django.urls import path

from MLCareApp import views

urlpatterns = [
    path('index/', views.index, name='index')
]