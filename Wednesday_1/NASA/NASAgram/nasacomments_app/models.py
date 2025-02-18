from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Comment(models.Model):
    image = models.TextField(validators=[URLValidator()])
    comment = models.CharField(max_length = 300)
    rating = models.IntegerField(default = 0)