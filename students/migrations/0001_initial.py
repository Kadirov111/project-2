# Generated by Django 5.1.3 on 2024-11-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_birth', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
            ],
        ),
    ]