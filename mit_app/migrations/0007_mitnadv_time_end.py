# Generated by Django 3.0 on 2019-12-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mit_app', '0006_auto_20191217_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitnadv',
            name='time_end',
            field=models.TimeField(blank=True, null=True),
        ),
    ]