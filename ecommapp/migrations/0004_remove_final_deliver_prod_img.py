# Generated by Django 4.2.5 on 2023-09-29 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0003_remove_final_deliver_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='final_deliver',
            name='prod_img',
        ),
    ]
