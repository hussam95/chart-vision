from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='predict-home'),
    path('predict/', views.predict, name='predict-patterns'),
    

]
