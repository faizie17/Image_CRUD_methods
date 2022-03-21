from django.db import models

class Products(models.Model):  
    productname = models.CharField(max_length=100)  
    productprice = models.CharField(max_length=200) 
    productquantity = models.CharField(max_length=200)  
    productimage = models.ImageField(upload_to='images/')
    class Meta:
         db_table= 'product'
         
class Title(models.Model):
    Title = models.CharField(max_length=100)
    items = models.ImageField(upload_to='items/',null=True)
    def __str__(self):
        return self.title

class Item(models.Model):  
    Title = models.ForeignKey(Title, on_delete= models.CASCADE, null= True)  
    image = models.ImageField(upload_to='items/',null=True)
    
class Category(models.Model):  
    category_name = models.CharField(max_length=100)  
    def __str__(self):
        return self.category_name