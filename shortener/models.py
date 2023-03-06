from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.URLField(max_length=200)
    new_link = models.URLField(default="")
    expire_time = models.DateTimeField("만료일", auto_now_add=True, null=False)