# Generated by Django 3.2 on 2022-11-03 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20221103_1310'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sport',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]