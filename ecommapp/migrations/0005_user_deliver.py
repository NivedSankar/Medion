# Generated by Django 4.2.5 on 2023-10-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0004_remove_final_deliver_prod_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_deliver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('est_del_date', models.DateField(null=True)),
                ('med_pic', models.CharField(max_length=200)),
                ('med_name', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
