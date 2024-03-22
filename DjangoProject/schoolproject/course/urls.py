from django.urls import path
from . import views
from . import views as vw

from .views import math_operation

urlpatterns = [
    path("learn_django",views.learn_django),
    path("learn_react",views.learn_react),
    path("learn_python",vw.learn_python),
    path("math_operation",math_operation),
]