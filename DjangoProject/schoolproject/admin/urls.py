from django.urls import path
from . import views
from . import views as vw

from .views import admin_react

urlpatterns = [
    path("admin_django",views.admin_django),
    path("admin_react",admin_react),
    path("admin_python",vw.admin_python),
]