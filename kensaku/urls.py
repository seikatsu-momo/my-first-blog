from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index,name='index'),
    path('find',views.find,name='find'),
    path('k_find',views.katasiki_find,name='k_find')
=======
    path('index', views.index,name='index'),
    path('',views.find,name='find')
>>>>>>> a337fb2a7f9fdba6e83f32597198a25237f90b9c
]