from django.db import models
from django import forms
from django.urls import reverse

from mezzanine.core.models import Displayable, Ownable, RichText


class Tag(models.Model):
    """
    модель тегов для поста
    """
    title = models.CharField(max_length=255, verbose_name='Тег')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class BlogPost(Displayable, Ownable, RichText):
    """
    модель поста
    """
    tag = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ("-publish_date",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        возвращает абсолютный урл education_blog_post_detail с slug на конце
        """
        return reverse("education_blog_post_detail", kwargs={"slug": self.slug})
