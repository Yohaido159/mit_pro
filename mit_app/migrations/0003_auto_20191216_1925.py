# Generated by Django 3.0 on 2019-12-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mit_app', '0002_auto_20191216_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mitnadv',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uplaod/'),
        ),
    ]
