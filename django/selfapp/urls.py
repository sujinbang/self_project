
from django.urls import include, path

from selfapp import views

urlpatterns = [
    path('test/', views.test),
]
