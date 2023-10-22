from django.http import HttpResponse
from ecommerce.inventory.models import ProductInventory, Product, Media
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format


def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))



def home(request):
    print(request)
    x = ProductInventory.objects.filter(product_id=1)
    print(sql(x))
    for i in x: 
        print(i)
    return HttpResponse("Hello, world.")
    