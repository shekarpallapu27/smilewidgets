from django.contrib import admin

#Register your models here.
from products.models import *

admin.site.register(Product)
admin.site.register(GiftCard)
admin.site.register(ProductPrice)
