# Generated by Django 3.2.10 on 2021-12-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]