# Generated by Django 3.0.7 on 2020-07-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tollywood', '0002_auto_20200709_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tollywood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=30)),
                ('heroname', models.CharField(max_length=60)),
                ('heroinename', models.CharField(max_length=80)),
                ('director', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=70)),
                ('cast', models.CharField(max_length=300)),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
