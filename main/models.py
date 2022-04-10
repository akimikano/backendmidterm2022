from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    title = models.CharField(max_length=255, verbose_name='title')
    text = models.TextField(verbose_name='text')
    date = models.DateField(auto_now_add=True, verbose_name='date')

    def __str__(self):
        return self.title