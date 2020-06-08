from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name='Наименование', max_length=80, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Наименование', max_length=80, blank=True)

    def __str__(self):
        return str(self.category) + ' ' + self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Article(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name='Наименование', max_length=80, blank=True)
    text = models.TextField(verbose_name='Текст статьи', )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Product(models.Model):
    objects = models.Manager()
    model = models.CharField(verbose_name='Модель', max_length=80, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    image = models.CharField(verbose_name='Картинка', max_length=128, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.CASCADE, blank=True, null=True)
    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(verbose_name='Slugify URL', max_length=10, unique=True)

    def __str__(self):
        return f'{self.model}'

    def sluggg(self):
        return slugify(self.model)

    def save(self, *args, **kwargs):
        self.slug = self.sluggg()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

