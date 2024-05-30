from django.urls import path
from .views import *

urlpatterns = [
   path('edit/<int:pk>/', edit, name='edit'),
  path('update/', update, name='update'), 
   path('delet/<int:pk>/', delet, name='delet'),

]