# Generated by Django 4.1.4 on 2022-12-09 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_ingredients', '0002_alter_active_ingredient_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='active_ingredient',
            name='mediums',
        ),
    ]
