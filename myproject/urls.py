from django.urls import path
from generator import views

urlpatterns = [
   path('easy/', views.easy_password),
   path('medium/', views.medium_password),
   path('hard/', views.hard_password),
]