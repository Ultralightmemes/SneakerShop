from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=50)
    country_founded = models.CharField(max_length=100)
    year_founded = models.DateField('Year founded')
    official_name = models.CharField(max_length=200)
    official_address = models.CharField(max_length=200)
    importer_name = models.CharField('Importer', max_length=200)
    importer_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Sneaker(models.Model):
    model_name = models.CharField(max_length=100)
    prod_country = models.CharField(max_length=50)
    cost = models.FloatField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='sneaker/%Y/%m/%d/', null=True, blank=True)
    material = models.CharField(max_length=100)
    inner_material = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=9)
    color = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.brand.name + ' ' + self.model_name


class Size(models.Model):
    eur_size = models.CharField(max_length=20, default=40)
    ru_size = models.CharField(max_length=20, default=40)
    sm_size = models.CharField(max_length=20, default=20)
    sneaker = models.ForeignKey('Sneaker', on_delete=models.CASCADE, null=True)
    count = models.IntegerField()

    def __str__(self):
        return self.eur_size
