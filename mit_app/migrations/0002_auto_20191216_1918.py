# Generated by Django 3.0 on 2019-12-16 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mit_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='mitnadv',
            name='gander',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='mitnadv',
            name='snif',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mit_app.Snif'),
        ),
    ]