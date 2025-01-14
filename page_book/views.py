from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from .models import *


menu = ['главная', 'регистрация', '']

def start_page(request):
    cats = Category.objects.all()
    post = Article.objects.all()
    data  = { 'menu': menu, 'title': 'Главная cтраница', 'post': post, "cats": cats, 'cat_selected': 0 }

    return render(request,'page_book/start_page.html', context=data)



def add_page(request):
    return render(request, 'page_book/new_page.html')



def show_post(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    return render(request, )


def show_category(request, cat_id):
    return HttpResponse(f"отображение категории {cat_id}")