# Generated by Django 4.0.6 on 2022-07-12 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0004_alter_sneaker_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='sneakers',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sneakers',
        ),
        migrations.RemoveField(
            model_name='size',
            name='size',
        ),
        migrations.RemoveField(
            model_name='sneaker',
            name='sizes',
        ),
        migrations.AddField(
            model_name='size',
            name='eur_size',
            field=models.CharField(default=40, max_length=20),
        ),
        migrations.AddField(
            model_name='size',
            name='ru_size',
            field=models.CharField(default=40, max_length=20),
        ),
        migrations.AddField(
            model_name='size',
            name='sm_size',
            field=models.CharField(default=20, max_length=20),
        ),
        migrations.AddField(
            model_name='size',
            name='sneaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sneakers.sneaker'),
        ),
        migrations.AddField(
            model_name='sneaker',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sneakers.brand'),
        ),
        migrations.AddField(
            model_name='sneaker',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sneakers.category'),
        ),
    ]
