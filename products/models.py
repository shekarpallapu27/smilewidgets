from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25, help_text='Customer facing name of product')
    code = models.CharField(max_length=10, help_text='Internal facing reference to product')
    price = models.PositiveIntegerField(help_text='Price of product in cents')
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.formatted_amount)
 
    @property
    def formatted_amount(self):
        return '${0:.2f}'.format(self.price / 100)

class GiftCard(models.Model):
    code = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(help_text='Value of gift card in cents')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.code, self.formatted_amount)
    
    @property
    def formatted_amount(self):
        return '${0:.2f}'.format(self.amount / 100)


class ProductPrice(models.Model):
    product_price_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product,related_name="product_productpricedetails",on_delete=models.PROTECT)
    schedule_price = models.CharField(max_length=10,help_text='Price of product in cents')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)


    def __str__(self):
        return '{} - {}'.format(self.product_id.name,self.formatted_amount)

    @property
    def formatted_amount(self):
        if self.schedule_price!='FREE':
            return '${0:.2f}'.format(int(self.schedule_price)/100)
        else:
            return self.schedule_price

