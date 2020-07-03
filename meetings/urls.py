from django.contrib import admin
from django.urls import path
from .views import detail,roomdetail,new

urlpatterns = [
    path('<int:id>',detail,name="detail"),
    path('roomdetail',roomdetail,name="roomdetail"),
    path('new',new)
]