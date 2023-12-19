from django.urls import path 
  
# importing views from views..py 
from .views import base
  
urlpatterns = [ 
    path('', base, name='base' ), 
] 