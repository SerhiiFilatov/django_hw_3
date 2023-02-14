from users.models import User_model
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Headings(models.Model):

    name = models.CharField(max_length=100, db_index=True, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)

class Post(models.Model):

    rubric = models.ForeignKey(Headings,max_length=100, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=64, blank=True, editable=False, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    content = models.TextField(verbose_name='Зміст')
    created = models.DateField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateField(auto_now=True, verbose_name='Оновлено')

    class Meta():
        verbose_name_plural = 'Дописи'

    def get_absolute_url(self):
        return reverse('object_slug', kwargs={'p_slug': self.slug})

    def __str__(self):
        return '%s' % (self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)





