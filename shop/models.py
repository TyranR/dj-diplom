from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.text import slugify
from pytils.translit import slugify

from shop.managers import MyUserManager


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name='Наименование', max_length=80, blank=True)
    slug = models.SlugField(verbose_name='Slugify URL', max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def sluggg(self):
        return slugify(self.name)

    def save(self, *args, **kwargs):
        self.slug = self.sluggg()
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Наименование', max_length=80, blank=True)
    slug = models.SlugField(verbose_name='Slugify URL', max_length=10, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.category) + ' ' + self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def sluggg(self):
        return slugify(self.name)

    def save(self, *args, **kwargs):
        self.slug = self.sluggg()
        super().save(*args, **kwargs)


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
    subcategory = models.ForeignKey(SubCategory, verbose_name='Подкатегория', on_delete=models.CASCADE, blank=True,
                                    null=True)
    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(verbose_name='Slugify URL', max_length=10, unique=True)
    rating = models.IntegerField(verbose_name='Рейтинг', blank=True, null=True)

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


class Review(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name='Имя', max_length=20, blank=True, null=True)
    description = models.TextField(verbose_name='Содержание', )
    mark = models.IntegerField(verbose_name='Оценка', )
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.product.model) + ' ' + str(self.description)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete = models.CASCADE)
    pr_count = models.IntegerField()

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete = models.CASCADE)
    pr_count = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'account_' + self.user.email + '__product_' + self.product.model + '_' + str(self.pr_count) + '_pcs'
