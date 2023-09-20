from django.db import models
from django.contrib.auth.models import User


class LessonTopic(models.Model):
    lesson_name = models.CharField(max_length = 150)
    url_video = models.URLField()
    time_of_watching = 
    status_from_user = models.CharField(max_length = 150, default = 'Не просмотренно')

    def __str__(self):
        return self.lesson_name

class Product(models.Model):
    product_name = models.CharField(max_length = 150)
    user_own = models.ForeignKey(User, on_delete = models.CASCADE)
    lesson_to_product = models.ManyToManyField(LessonTopic)

    def __str__(self):
        return self.product_name    
