# Generated by Django 4.2 on 2023-06-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=12)),
                ('pass1', models.CharField(max_length=40)),
                ('pass2', models.CharField(max_length=40)),
            ],
        ),
    ]
