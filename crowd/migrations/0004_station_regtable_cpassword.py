# Generated by Django 3.2.7 on 2024-04-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowd', '0003_remove_station_regtable_cpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='station_regtable',
            name='cpassword',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
