from . import views
from django.urls import path, include

urlpatterns = [
    path("",views.hello_world,name="hello_sample")
]