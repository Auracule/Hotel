# Generated by Django 4.0.6 on 2022-07-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_category_description_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description_c',
            field=models.TextField(),
        ),
    ]
