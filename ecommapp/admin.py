from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(reg_seller)
admin.site.register(reg_buyer)
admin.site.register(product_add)
admin.site.register(wishlist)
admin.site.register(cart)
admin.site.register(address_buyer)
admin.site.register(delivery_details)
admin.site.register(final_deliver)
