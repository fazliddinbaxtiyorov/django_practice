from django.urls import path
from generator import views

urlpatterns = [
   path('<str:name>/', views.generate_password),
]
