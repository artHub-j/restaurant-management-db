# Generated by Django 5.0.6 on 2024-06-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('la_burguesa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleat',
            name='dni',
            field=models.CharField(max_length=22, primary_key=True, serialize=False),
        ),
    ]
