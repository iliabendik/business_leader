from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompaniesView.as_view(), name = 'home')
]
