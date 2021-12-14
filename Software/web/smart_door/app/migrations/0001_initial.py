# Generated by Django 3.2.7 on 2021-12-14 10:42

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('uid', models.CharField(default='', max_length=20, verbose_name='用户id')),
                ('face_num', models.IntegerField(default=0, verbose_name='人脸数')),
            ],
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
