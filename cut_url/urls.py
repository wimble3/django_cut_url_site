from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<slug:token>', url_catcher)
]
