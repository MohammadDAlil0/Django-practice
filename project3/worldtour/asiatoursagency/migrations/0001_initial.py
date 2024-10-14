# Generated by Django 5.1.2 on 2024-10-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_country', models.CharField(max_length=64)),
                ('destination_country', models.CharField(max_length=64)),
                ('number_of_nights', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
