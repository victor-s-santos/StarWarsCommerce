# Generated by Django 2.1.5 on 2021-05-28 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_auto_20210528_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='multiple',
            field=models.IntegerField(default=django.utils.timezone.now, verbose_name='Multiple'),
            preserve_default=False,
        ),
    ]
