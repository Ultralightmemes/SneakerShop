# Generated by Django 4.0.6 on 2022-07-23 20:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country_founded', models.CharField(max_length=100)),
                ('year_founded', models.DateField(verbose_name='Year founded')),
                ('official_name', models.CharField(max_length=200)),
                ('official_address', models.CharField(max_length=200)),
                ('importer_name', models.CharField(max_length=200, verbose_name='Importer')),
                ('importer_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('prod_country', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sneaker/%Y/%m/%d/')),
                ('material', models.CharField(max_length=100)),
                ('inner_material', models.CharField(max_length=100)),
                ('vendor_code', models.CharField(max_length=9)),
                ('color', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sneakers.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sneakers.category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eur_size', models.CharField(default=40, max_length=20)),
                ('ru_size', models.CharField(default=40, max_length=20)),
                ('sm_size', models.CharField(default=20, max_length=20)),
                ('count', models.IntegerField()),
                ('sneaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sneakers.sneaker')),
            ],
        ),
    ]
