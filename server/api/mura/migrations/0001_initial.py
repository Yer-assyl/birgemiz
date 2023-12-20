# Generated by Django 4.1.3 on 2022-11-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kaztitle', models.CharField(max_length=255)),
                ('rutitle', models.CharField(max_length=255)),
                ('entitle', models.CharField(max_length=255)),
                ('kazbody', models.TextField()),
                ('rubody', models.TextField()),
                ('enbody', models.TextField()),
                ('region', models.DecimalField(decimal_places=1, max_digits=10)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
    ]
