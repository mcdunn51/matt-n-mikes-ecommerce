# Generated by Django 2.1.7 on 2019-03-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_ipg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='IPGID',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
