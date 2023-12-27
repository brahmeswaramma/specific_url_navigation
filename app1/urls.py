from app1.views import *
from django.urls import path
app_name='hi'
urlpatterns=[
    path('First_World_War/',First_World_War,name='First_World_War'),
]