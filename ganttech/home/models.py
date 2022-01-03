from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.urls import reverse
from django.utils.safestring import mark_safe


class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand_images/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'



class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'



    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'




class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,  verbose_name='Наименование категории')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Цена')
    keywords = models.CharField(max_length=255, verbose_name='ключевые слова')
    description = models.TextField()
    detail = models.TextField()
    amount = models.IntegerField(default=0, verbose_name='Количество товара')
    minamount = models.IntegerField(default=3, blank=True, null=True, verbose_name='минимальная сумма')
    image = models.ImageField(upload_to='image')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title