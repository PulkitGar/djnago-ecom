from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(unique = True, max_length=50)
    slug = models.SlugField(unique=True,max_length=50)
    description = models.TextField(max_length=250, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)


    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])