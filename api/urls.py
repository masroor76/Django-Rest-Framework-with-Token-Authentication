from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentsView.as_view()),
]
