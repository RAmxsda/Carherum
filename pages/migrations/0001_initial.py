# Generated by Django 3.2 on 2023-01-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook_link', models.URLField(max_length=100)),
                ('twitter_link', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
