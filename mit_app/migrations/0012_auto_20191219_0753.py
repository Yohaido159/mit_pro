# Generated by Django 3.0 on 2019-12-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mit_app', '0011_auto_20191218_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift', models.CharField(choices=[('TE', 'teeth'), ('VE', 'vacation'), ('CL', 'clothes'), ('CO', 'course')], default='CL', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='PayForMounthModel',
        ),
    ]
