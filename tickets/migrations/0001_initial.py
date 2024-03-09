# Generated by Django 4.2.10 on 2024-03-08 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0004_movie_start_of_rolling_date'),
        ('screenings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('place', models.IntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screenings.screening')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
