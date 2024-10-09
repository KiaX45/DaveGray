from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120) # este campo es para el titulo del post
    body = models.TextField() # este campo es para el cuerpo del post
    slug  = models.SlugField() # este campo es para la url del post
    date = models.DateTimeField(auto_now_add=True) # este campo es para la fecha de creacion del post
    
    def __str__(self) -> str:
        return self.title