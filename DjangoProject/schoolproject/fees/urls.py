from django.urls import path
from . import views
from . import views as vw

from .views import fees_react

urlpatterns = [
    path("fees_django",views.fees_django),
    path("fees_react",fees_react),
    path("fees_python",vw.fees_python),
]