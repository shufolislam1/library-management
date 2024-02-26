from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    catagory = models.ForeignKey(Catagory,on_delete = models.CASCADE)
    title = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField()
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
    

# class Comment(models.Model):
#     car =  models.ForeignKey(Car, on_delete = models.CASCADE, related_name='comment')
#     name = models.CharField(max_length = 50)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add = True)
    
#     def __str__(self):
#         return f"Commented by {self.name}"
    