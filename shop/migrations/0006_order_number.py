# Generated by Django 3.1 on 2020-06-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200612_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер заказа'),
            preserve_default=False,
        ),
    ]
