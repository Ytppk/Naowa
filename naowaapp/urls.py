from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/', views.search, name='search'),
    path('result/<slug:slug>/', views.result, name='result'),
    path('adddata/', views.adddata, name='adddata'),
]
