# Generated by Django 4.1.1 on 2022-10-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-03-02'),
            preserve_default=False,
        ),
    ]
