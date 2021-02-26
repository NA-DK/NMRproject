from django.urls import path

from . import views

app_name = 'nmr'

urlpatterns = [
    path('', views.formula_create, name='index'),
]