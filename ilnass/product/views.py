import json
import jwt
import bcrypt

from django.shortcuts  import render
from django.shortcuts  import render
from django.views      import View
from django.http       import JsonResponse

from django.db             import models
from .models               import (
    Products,
    DetailImage,
    Brand,
    Level,
    Introduction,
)

#전체 리스트
class Allproducts(View):
    def get(self,request):
        product_all = Products.objects.all()
        product_list = [{
            'thumbnail'        : product.thumbnail,
            'category'         : product.category,
            'name'             : product.name,
            'heart_count'      : product.heart_count,
            'like'             : product.like,
            'retail_price'     : product.retail_price,
            'discount_percent' : product.discount_percent,
            'monthly_pay'      : product.monthly_pay,
            'monthly_payment'  : product.monthly_payment,
        } for product in product_all]

        return JsonResponse({'data':product_list}, status=200)
#MD추천
class RecommendView(View):
    def get(self,request):
        recommend_products = Products.objects.filter(like__gt = 92)
        recommend_product = [{
            'thumbnail'        : product.thumbnail,
            'category'         : product.category,
            'name'             : product.name,
            'heart_count'      : product.heart_count,
            'like'             : product.like,
            'retail_price'     : product.retail_price,
            'discount_percent' : product.discount_percent,
            'monthly_pay'      : product.monthly_pay,
            'monthly_payment'  : product.monthly_payment,
        }for product in recommend_products]

        return JsonResponse({'data':recommend_product}, status=200)

#디테일
class DetailView(View):
    def get(self,request):
        product = Products.objects.get(id=1)
        product_detail = [{
            'category'         : product.category,
            'name'             : product.name,
            'monthly_payment'  : product.monthly_payment,
            'monthly_pay'      : product.monthly_pay,
            'discount_percent' : product.discount_percent,
            'heart_count'      : product.heart_count,
            # p = Products.objects.get(id=1)
            # n = p.end_datetime
            # new_n = n.strftime("%Y-%m-%d %H:%M:%S")
        }for product in recommend_products]

        return JsonResponse({'data':product_detail}, status=200)

class Basicinformation(View):
    def post(self, request):
        # information = request.GET.get('information', None)
        data = json.loads(request.body)
        
        introduction(
            brand           = data['brand'],
            category        = data['category'],
            detail_category = data['detail_category'],
            level           = data['level'],
        ).save()
        

        return JsonResponse({'message':'SUCCESS'}, status=200)


        
        
        