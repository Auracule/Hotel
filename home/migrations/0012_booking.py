# Generated by Django 4.0.6 on 2022-07-22 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_b', models.FloatField()),
                ('check_in', models.DateField(auto_now=True)),
                ('check_out', models.DateField(auto_now=True)),
                ('no_days', models.CharField(max_length=50)),
                ('book_no', models.BooleanField()),
                ('no_room', models.IntegerField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
