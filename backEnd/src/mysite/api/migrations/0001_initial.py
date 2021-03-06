# Generated by Django 2.1.5 on 2019-02-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemno', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('description2', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('colour', models.CharField(max_length=50)),
                ('manufacturerCode', models.CharField(max_length=50)),
            ],
        ),
    ]
