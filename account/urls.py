from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', reg, name='reg'),
    path('authorization/', auth, name='auth'),
]
