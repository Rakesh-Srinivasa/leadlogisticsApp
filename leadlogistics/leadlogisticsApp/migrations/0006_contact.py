# Generated by Django 3.0.5 on 2020-08-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadlogisticsApp', '0005_auto_20200815_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('subject', models.CharField(max_length=256)),
                ('requirements', models.TextField()),
            ],
        ),
    ]
