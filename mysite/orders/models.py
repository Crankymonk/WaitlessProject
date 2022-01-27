from django.db import models
from service.models import Item, Staff
# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    table_id = models.IntegerField(default=None)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    RoomType = models.TextChoices('RoomType', 'BAR MAIN CHILLOUT')
    room = models.CharField(blank=True, choices=RoomType.choices, max_length=10)
    served = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Item,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class CallItem(models.Model):
    worker = models.CharField(max_length=250)
    order = models.ForeignKey(Order,
                              default='123',
                              related_name='order',
                              on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)