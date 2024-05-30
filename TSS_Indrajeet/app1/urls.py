from django.urls import path
from .views import*

urlpatterns = [
  path('', home, name='home'),
  path('insert/', insert, name='insert'),
  path('show/', show, name='show'),
]