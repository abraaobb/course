# Generated by Django 4.0.4 on 2022-05-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='asd',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
