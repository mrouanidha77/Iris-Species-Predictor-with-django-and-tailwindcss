# Generated by Django 5.0.3 on 2024-03-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iris_prediction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='confidence',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='prediction',
            name='model_used',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='predicted_class',
            field=models.CharField(max_length=100),
        ),
    ]
