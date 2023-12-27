from app2.views import *
from django.urls import path
app_name='hello'
urlpatterns=[
    path('Second_World_War/',Second_World_War,name='Second_World_War')
]