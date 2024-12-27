# Generated by Django 5.1.4 on 2024-12-27 02:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('imdb', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('payment_method', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('seats_available', models.IntegerField(default=25)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='index.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('is_booked', models.BooleanField(default=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='index.showtime')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('payment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='index.payment')),
                ('seats', models.ManyToManyField(related_name='bookings', to='index.seat')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='index.showtime')),
            ],
        ),
    ]
