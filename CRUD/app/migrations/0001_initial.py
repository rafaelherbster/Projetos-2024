# Generated by Django 5.0.1 on 2024-01-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=150)),
                ('modelo', models.CharField(max_length=150)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
