# Generated by Django 4.1.5 on 2023-01-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='demand', max_length=100, verbose_name='title')),
                ('text', models.TextField(default=None, verbose_name='text')),
                ('graph_first', models.ImageField(default=None, upload_to='demand', verbose_name='graph_first')),
                ('graph_second', models.ImageField(default=None, upload_to='demand', verbose_name='graph_second')),
            ],
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='geography', max_length=100, verbose_name='title')),
                ('text', models.TextField(default=None, verbose_name='text')),
                ('table', models.TextField(default=None, verbose_name='table')),
                ('graph', models.ImageField(default=None, upload_to='geography', verbose_name='graph')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='homepage', max_length=100, verbose_name='title')),
                ('text', models.TextField(default=None, verbose_name='text')),
                ('image', models.ImageField(default=None, upload_to='home', verbose_name='img')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='skills', max_length=100, verbose_name='title')),
                ('text', models.TextField(default=None, verbose_name='text')),
                ('graph', models.ImageField(default=None, upload_to='skills', verbose_name='graph')),
            ],
        ),
    ]
