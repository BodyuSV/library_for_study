from time import monotonic_ns

from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(max_length=10000, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='логотип статьи')
    file = models.FileField(blank=True, upload_to='file/%Y/%m/%d/', verbose_name='Прикрепленный файл')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'time_create']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=300, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['name']




