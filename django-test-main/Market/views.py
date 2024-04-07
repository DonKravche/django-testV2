from django.shortcuts import render

import Market
from Market.models import Books
from django.http import JsonResponse


# Create your views here.

def get_products(request):
    products = Books.objects.all()
    item = []
    for items in products:
        item.append({
            'name': items.name,
            'page_count': items.page_count,
            'category': items.category,
            'author_name': items.author_name,
            'price': items.price,
            # 'image': items.image
        })

    return JsonResponse(item, safe=False)


def get_product(request, product_id):
    product = Books.objects.get(pk=product_id)
    item = {
        'name': product.name,
        'page_count': product.page_count,
        'category': product.category,
        'author_name': product.author_name,
        'price': product.price,
        # 'image': product.image
    }
    return JsonResponse(item)
