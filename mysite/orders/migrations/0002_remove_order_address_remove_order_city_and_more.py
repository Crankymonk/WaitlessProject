# Generated by Django 4.0.1 on 2022-01-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='room',
            field=models.CharField(blank=True, choices=[('BAR', 'Bar'), ('MAIN', 'Main'), ('CHILLOUT', 'Chillout')], max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='served',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='table_id',
            field=models.IntegerField(default=None),
        ),
    ]
