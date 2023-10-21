from django.http import HttpResponse
from ecommerce.inventory.models import ProductInventory



def home(request):
    print(request)
    x = ProductInventory.objects.filter(product_id=1)
    for i in x: 
        print(i)
    return HttpResponse("Hello, world.")
    