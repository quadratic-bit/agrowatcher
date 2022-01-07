from django.urls import path
from backend.core import views

urlpatterns = [
    path('ping/', views.ping)
]
