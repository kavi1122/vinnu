from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[
    path('app1_machi/',app1_machi,name='app1_machi'),
]