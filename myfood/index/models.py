from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_photo = models.CharField(default='https://worldfoodtour.co.uk/wp-content/uploads/2013/06/neptune-placeholder-48.jpg')

    def __str__(self):
        return self.item_name