# Generated by Django 4.2.5 on 2023-10-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0006_user_deliver_city_user_deliver_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_deliver',
            name='dosage',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
