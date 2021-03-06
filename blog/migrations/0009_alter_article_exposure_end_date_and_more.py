# Generated by Django 4.0.5 on 2022-06-24 06:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_exposure_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='exposure_end_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 24, 6, 23, 55, 94622, tzinfo=utc), verbose_name='노출 시작 일자'),
        ),
        migrations.AlterField(
            model_name='article',
            name='exposure_start_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 24, 6, 23, 55, 94622, tzinfo=utc), verbose_name='노출 시작 일자'),
        ),
    ]
