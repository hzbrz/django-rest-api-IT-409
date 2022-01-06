from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

# Create your models here.
class Customer(models.Model):
    PRIME = [
        (True, 'Y'),
        (False, 'N')
    ]
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    customer_since = models.DateField(auto_now_add=True, null=False)
    prime_customer = models.CharField(max_length=1, choices=PRIME, default='N', null=False)

    def __str__(self):
        return 'customer id: ' + str(self.id) + self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name']  # asc

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    street = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, null=False)
    zip = models.CharField(max_length=10, null=False)

    def __str__(self):  # String representation
        return self.street + ' ' + self.city + ' ' + self.state + ' ' + self.zip

    class Meta:
        ordering = ['zip']  # asc

class Order(models.Model):
    P_TYPE = [
        ('C', 'Credit'),
        ('B', 'Bank Account'),
        ('O', 'Other Types')
    ]
    c = date.today()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    order_num = models.CharField(max_length=10, null=False)
    order_date = models.DateField(default=date.today())
    order_total = models.FloatField(null=False, validators=[MinValueValidator(0.0)])
    payment_type = models.CharField(null=False, choices=P_TYPE, max_length=1)
    account_number = models.CharField(null=False, max_length=20)
    expiration_date = models.DateField(default=date(c.year + 1, c.month, c.day), null=False)

    def __str__(self):
        return 'order id:' + str(self.id) + str(self.customer)

    class Meta:
        order_with_respect_to = 'customer'

class OrderItem(models.Model):
    ITEMS = [
        ('Java 101', 'Java 101'),
        ('Python 101', 'Python 101'),
        ('Biology 101', 'Biology 101'),
        ('English 101', 'English 101'),
        ('Cloud Computing 101', 'Cloud Computing 101')
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    item_description = models.CharField(null=False, choices=ITEMS, max_length=25)
    item_quantity = models.IntegerField(null=False)

    def __str__(self):
        return 'order item id: ' + str(self.id) + ' order id: ' + str(self.order.id)

    class Meta:
        order_with_respect_to = 'order'
