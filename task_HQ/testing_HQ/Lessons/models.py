from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length = 150)
    user_own = models.ForeignKey(User, related_name = 'own', on_delete = models.CASCADE)
    user_access = models.ManyToManyField(User, related_name = 'access', blank = True)
    
    def __str__(self):
        return self.product_name   

class LessonTopic(models.Model):
    lesson_name = models.CharField(max_length = 150)
    watched_by_user = models.ManyToManyField(User, blank = True)
    video_url = models.URLField(max_length = 150)
    lesson_to_product = models.ManyToManyField(Product, blank = True)

    def __str__(self):
        return self.lesson_name

 
