from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service:item_list_by_category', args=[self.slug])


class Item(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='items',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)
    available = models.BooleanField(default=True)
    class Meta:
        ordering = ('name',)
        index_together = (('slug', 'id'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service:item_detail', args=[self.slug, self.id])


class Staff(models.Model):
    name = models.CharField(default='Andrei', max_length=200, db_index=True)
    position = models.CharField(default='shishamaster', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
