from tkinter.font import names

from django.urls import path, include
from .views import start_page, add_page, show_post, show_category

urlpatterns = [
    path('', start_page, name='home'),
    path('add_page', add_page, name='add_page'),
    path("post/<int:post_id>/", show_post, name='post'),
    path('cat/<int:cat_id>/', show_category, name='cat')
]