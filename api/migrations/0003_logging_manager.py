# Generated by Django 2.1.5 on 2019-03-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_logging_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='logging',
            name='manager',
            field=models.CharField(default='A', max_length=10),
            preserve_default=False,
        ),
    ]
