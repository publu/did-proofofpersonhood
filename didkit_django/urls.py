from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('credential/', views.credential, name='credential'),
    path('did.json', views.well_known, name='well-known'),
]
