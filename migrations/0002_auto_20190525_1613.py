# Generated by Django 2.2 on 2019-05-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneyrecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='money',
            field=models.IntegerField(help_text='Currency = JPY', verbose_name='Amount'),
        ),
    ]