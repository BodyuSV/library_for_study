from django.shortcuts import render
from django.http import HttpResponse


menu = ['главная', 'регистрация']
def start_page(request):
    data  = { 'menu': menu, 'title': 'Главная втраница' }
    return render(request,'page_book/start_page.html', context=data)
