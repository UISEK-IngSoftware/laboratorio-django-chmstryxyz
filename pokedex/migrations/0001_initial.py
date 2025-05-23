# Generated by Django 4.2 on 2025-05-20 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('base_experience', models.IntegerField()),
                ('types', models.CharField(max_length=100)),
                ('abilities', models.CharField(max_length=100)),
                ('stats', models.CharField(max_length=100)),
            ],
        ),
    ]
