from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('app2_machi/',app2_machi,name='app2_machi'),
]