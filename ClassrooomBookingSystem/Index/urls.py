from django.urls import path
from . import views     # import local app view

urlpatterns = [
    path('', views.index_page, name='Index-Page'),
]