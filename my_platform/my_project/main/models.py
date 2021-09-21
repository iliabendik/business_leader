from django.db import models
from django import forms

class Category(models.Model):
    name = models.CharField('Категория', max_length=50)
    url = models.SlugField('Url', max_length=100, default = '', unique = True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class City(models.Model):
    name = models.CharField('Город', max_length=50)
    url = models.SlugField('Url', max_length=100, default='', unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Uslugi_dla_biznesa(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Услуги для бизнеса'
        verbose_name_plural = 'Услуги для бизнеса'

class Tovari_dla_biznesa(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товары для бизнеса'
        verbose_name_plural = 'Товары для бизнеса'

class Investicii(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Инвестиции'
        verbose_name_plural = 'Инвестиции'

class Kommercheskie_tenderi(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Коммерческие тендеры'
        verbose_name_plural = 'Коммерческие тендеры'

class Meri_podderjki(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Меры поддержки'
        verbose_name_plural = 'Меры поддержки'

class Pervaya_socialnaya_birja(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Первая социальная биржа'
        verbose_name_plural = 'Первая социальная биржа'

class Socialnie_projekti(models.Model):
    name = models.CharField('Категория', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Социальные проекты'
        verbose_name_plural = 'Социальные проекты'


class Company(models.Model):
    title = models.CharField('Название фирмы', max_length=50)
    description = models.TextField('Описание фирмы')
    category_uslugi_dla_biznesa = models.ManyToManyField(Uslugi_dla_biznesa, 'Услуги_для_бизнеса', blank=True)
    category_tovari_dla_biznesa = models.ManyToManyField(Tovari_dla_biznesa, 'Товары_для_бизнеса', blank=True)
    place = models.ManyToManyField(City, 'Города')
    image = models.ImageField('Картинка фирмы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'