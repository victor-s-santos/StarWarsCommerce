# Generated by Django 2.1.5 on 2021-05-27 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20210527_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='multiple',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Multiple'),
        ),
    ]
