# Generated by Django 3.0.7 on 2020-07-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200716_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='imagen'),
        ),
    ]
