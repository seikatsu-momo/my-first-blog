from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('find',views.find,name='find'),
    path('k_find',views.katasiki_find,name='k_find')
]