# Generated by Django 3.1.6 on 2021-02-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formula_13C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=200)),
                ('cid', models.IntegerField()),
                ('structure_imageurl', models.ImageField(upload_to='')),
                ('cnmr_imageurl', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Formula_1H',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=200)),
                ('cid', models.IntegerField()),
                ('structure_imageurl', models.ImageField(upload_to='')),
                ('hnmr_imageurl', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Name_13C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cid', models.IntegerField()),
                ('structure_imageurl', models.TextField()),
                ('cnmr_imageurl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Name_1H',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cid', models.IntegerField()),
                ('structure_imageurl', models.TextField()),
                ('hnmr_imageurl', models.TextField()),
            ],
        ),
    ]
