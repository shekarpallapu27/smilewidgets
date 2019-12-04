from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from products.models import *
from datetime import datetime

class ProductDetails(APIView):

    def formatted_amount(self,schedule_price):
        if schedule_price!='FREE':
            return '${0:.2f}'.format(int(schedule_price)/100)
        else:
            return schedule_price

    def get(self,request):
        try:
            prod_id = request.GET.get('product_code')
            prod_date = request.GET.get('date')
            gift = request.GET.get('gift')
            if prod_id and prod_date:
                date_str_fmt='%d-%m-%Y'
                date_obj = datetime.strptime(prod_date,date_str_fmt)
                prod_srt_obj = ProductPrice.objects.filter(product_id__code=prod_id,date_start__lte=date_obj,date_end__isnull=True)
                if prod_srt_obj:
                    if date_obj>= datetime(day=prod_srt_obj[0].date_start.day,month=prod_srt_obj[0].date_start.month,year=prod_srt_obj[0].date_start.year):
                        prod_end_obj = ProductPrice.objects.filter(product_id__code=prod_id,date_start__lte=date_obj,date_end__gte=date_obj)
                        if prod_end_obj:
                            price = self.formatted_amount(prod_end_obj[0].schedule_price)
                            return Response(price)
                        else:
                            price = self.formatted_amount(prod_srt_obj[0].schedule_price)
                            return Response(price)
                    else:
                        prod_obj = Product.objects.filter(code=prod_id)
                        price = self.formatted_amount(prod_end_obj[0].price)
                        return Response(price)
                else:
                    prod_obj = Product.objects.filter(code=prod_id)
                    price = self.formatted_amount(prod_obj[0].price)
                    return Response(price)
            else:
                return Response("required product code and product date")
        except:
            return Response("failed")