# Generated by Django 3.1.7 on 2021-10-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20211030_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='van',
            name='color',
        ),
        migrations.AlterField(
            model_name='van',
            name='enStatus',
            field=models.CharField(choices=[('y', 'Working'), ('n', 'Not working')], default='NA', max_length=50),
        ),
    ]
