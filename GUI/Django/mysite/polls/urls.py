from django.urls import path, include
from . import views
urlpatterns = [
    path('/hi', views.index)

]









