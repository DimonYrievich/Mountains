# Generated by Django 4.2.3 on 2023-07-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Point', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new', max_length=20),
        ),
    ]