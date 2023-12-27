from app3.views import *
from django.urls import path
app_name='hello django'
urlpatterns=[
    path('Kings/',Kings,name='Kings')
]