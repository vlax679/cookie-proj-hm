# Generated by Django 4.1.6 on 2023-04-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('cost', models.TextField(max_length=20)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
