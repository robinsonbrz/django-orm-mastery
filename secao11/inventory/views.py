from django.http import HttpResponse

from inventory.models import Brand, Category
from django.db import connection
from django.db import reset_queries, IntegrityError


def new(requests):
    brand = Brand.objects.all()
    brand[0].nickname = "nickname"
    brand[0].save()
    
    print(brand[0].name)
    print(brand[0].nickname)
    return HttpResponse(f"Brand: {brand[0].name}\n Nickname: {brand[0].nickname}\n")

def new2(requests):
    try:
        name_brand="Nike4"
        Brand.objects.create(brand_id=4,name=name_brand)
        print("Brand created")
    except IntegrityError:
        print(len(Brand.objects.all()))
        return HttpResponse("Brand already exists")

    return HttpResponse(f"Category: Saved")
