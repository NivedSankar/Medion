from django.db import models

# Create your models here.

class reg_seller(models.Model):
    sname = models.CharField(max_length=30)
    email = models.EmailField()
    img_name = models.FileField(upload_to='ecommapp/static/images')
    phone = models.BigIntegerField()
    cname = models.CharField(max_length=30)
    com_details = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.sname

class product_add(models.Model):
    man_name = models.CharField(max_length=30)
    med_name = models.CharField(max_length=30)
    dosage = models.CharField(max_length=30)
    choice = [
        ('baby','baby'),
        ('health', 'health'),
        ('women','women'),
        ('personal','personal'),
        ('ayurveda','ayurveda'),
        ('healthd','healthd'),
        ('home','home'),
        ('healthc','healthc')
        # ('Baby Care', 'Baby Care'),
        # ('Health and Drink Suppliments', 'Health and Drink Suppliments'),
        # ('Women Care', 'Women Care'),
        # ('Personal Care', 'Personal Care'),
        # ('Ayurveda', 'Ayurveda'),
        # ('Health Devices', 'Health Devices'),
        # ('Home Essentials', 'Home Essentials'),
        # ('Health Condition', 'Health Condition')

    ]
    type = models.CharField(max_length=30,choices=choice)
    qty = models.IntegerField()
    price = models.IntegerField()
    mtf = models.CharField(max_length=30)
    med_pic = models.FileField(upload_to='ecommapp/static/images')
    def __str__(self):
        return self.med_name

class reg_buyer(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    buyer_img = models.FileField(upload_to='ecommapp/static/images')
    phone = models.BigIntegerField()
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username

class wishlist(models.Model):
    user_id = models.IntegerField()
    prod_id = models.IntegerField()
    man_name1 = models.CharField(max_length=30)
    med_name1 = models.CharField(max_length=30)
    dosage1 = models.CharField(max_length=30)
    type1 = models.CharField(max_length=30)
    qty1 = models.IntegerField()
    price1 = models.IntegerField()
    mtf1 = models.CharField(max_length=30)
    med_pic1 = models.FileField()

    def __str__(self):
        return self.med_name1


class cart(models.Model):
    user_id = models.IntegerField()
    prod_id = models.IntegerField()
    man_name1 = models.CharField(max_length=30)
    med_name1 = models.CharField(max_length=30)
    dosage1 = models.CharField(max_length=30)
    type1 = models.CharField(max_length=30)
    qty1 = models.IntegerField()
    price1 = models.IntegerField()
    mtf1 = models.CharField(max_length=30)
    med_pic1 = models.FileField()


    def __str__(self):
        return self.med_name1


class address_buyer(models.Model):
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip = models.IntegerField()

    def __str__(self):
        return self.full_name


class delivery_details(models.Model):
    username = models.CharField(max_length=100)
    user_id = models.IntegerField()
    address = models.CharField(max_length=200)
    order_date = models.DateField(auto_now_add=True)
    est_del_date = models.DateField(null=True)
    products = models.CharField(max_length=200)
    prod_img = models.FileField()
    amount = models.IntegerField()
class final_deliver(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=200)
    order_date = models.DateField(auto_now_add=True)
    est_del_date = models.DateField(null=True)
    products = models.CharField(max_length=200)
    amount = models.IntegerField()





class user_deliver(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
    order_date = models.DateField(auto_now_add=True)
    est_del_date = models.DateField(null=True)
    med_pic = models.CharField(max_length=200)
    med_name = models.CharField(max_length=200)
    qty = models.CharField(max_length=30)
    dosage = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    amount = models.IntegerField()