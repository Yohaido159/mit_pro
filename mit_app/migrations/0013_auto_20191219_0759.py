# Generated by Django 3.0 on 2019-12-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mit_app', '0012_auto_20191219_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitnadv',
            name='gifts',
            field=models.ManyToManyField(to='mit_app.Gift'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='gift',
            field=models.CharField(max_length=30),
        ),
    ]