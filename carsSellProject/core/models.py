from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #profile_pic = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics/')
    country = models.CharField(default='Israel',max_length=100,null=False)
    phone_number = models.CharField(default='0',max_length=250,null=False)
    def get_num_posts(self):
        #i can user this without filtering Post.objects.all() - its for Home Page to petch all posts not for specific user.
        return Post.objects.filter(user=self).count()




class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    car_type =models.CharField(max_length=250,null=False)
    car_model=models.CharField(max_length=250,null=False)
    car_year = models.CharField(max_length=250,null=False)
    car_yad = models.CharField(max_length=50,null=False)
    car_pic = models.ImageField(blank=True,upload_to='profile_pics/')
    date_created = models.DateTimeField(auto_now_add=True,null= False)
    car_price = models.CharField(default='Not available',max_length=250,null=False)

    def __str__(self):
        return self.car_type + ' ' + self.car_model

