# Generated by Django 4.0.2 on 2022-02-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Discount', 'Discount'), ('Monthly', 'Monthly'), ('Weekly', 'Weekly'), ('Daily', 'Daily'), ('Free', 'Free')], default='Free', max_length=30),
        ),
    ]