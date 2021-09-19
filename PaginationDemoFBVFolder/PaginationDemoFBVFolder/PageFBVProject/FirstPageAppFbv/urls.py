from django.urls import path
from .views import studentpagination_view

urlpatterns = [
    path('show/',studentpagination_view, name='show'),
]