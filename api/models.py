from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # def __str__(self):
    #     return self.name