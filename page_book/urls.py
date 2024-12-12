from django.urls import path, include
from .views import start_page

urlpatterns = [
    path('', start_page)
]