# Generated by Django 4.0.6 on 2022-07-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_room_gallery1_alter_room_gallery2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gallery', models.ImageField(default='gallery.jpg', upload_to='gallery')),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='gallery1',
        ),
        migrations.RemoveField(
            model_name='room',
            name='gallery2',
        ),
        migrations.RemoveField(
            model_name='room',
            name='gallery3',
        ),
        migrations.RemoveField(
            model_name='room',
            name='gallery4',
        ),
    ]
