# Generated by Django 4.1 on 2022-11-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('INFORMATION', 'INFORMATION'), ('LIFE', 'LIFE'), ('VOYAGE', 'VOYAGE'), ('CULTURE', 'CULTURE'), ('OTHERS', 'OTHERS')], max_length=255),
        ),
    ]
