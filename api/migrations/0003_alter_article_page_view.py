# Generated by Django 3.2.6 on 2021-11-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='page_view',
            field=models.IntegerField(default=0, verbose_name='浏览量'),
        ),
    ]