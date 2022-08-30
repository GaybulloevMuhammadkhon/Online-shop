from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_price = models.FloatField(blank=True,null=True)
    product_description = models.TextField(blank=True,null=True)
    product_count = models.IntegerField(blank=True,null=True)
    product_added_date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='media',blank=True,null=True)


    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class UserCart(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'