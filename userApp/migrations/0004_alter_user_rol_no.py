# Generated by Django 4.2.13 on 2024-06-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_alter_user_rol_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol_no',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
