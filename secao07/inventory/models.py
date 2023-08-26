from django.db import models

class Brand(models.Model):
    # user defined id => auto increment number
    brand_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    the_name = models.CharField("Product Name", max_length=100, default="no-name", help_text="This is the help text")
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    inventory_received = models.BooleanField()

    class Meta:
        ordering = ["age"]
    
    def __str__(self):
        return f"Product name: {self.name}"

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

# class Product2(models.Model):
#     name = models.CharField(max_length=10)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     date_added = models.DateTimeField(auto_now_add=True) # When record is created
#     date_updated = models.DateTimeField(auto_now_add=True)  # every time the record is updated
#     url = models.SlugField()
#     is_active = models.BooleanField()
