from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    photo = models.ImageField(upload_to='image/%Y/%m/%d/')
    file = models.FileField(blank=True, upload_to='file/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_created=True)
    is_published = models.BooleanField(default=False)
