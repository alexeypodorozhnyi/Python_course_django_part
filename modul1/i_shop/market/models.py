from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='', null=True)
    profile_wallet = models.IntegerField(default=1000)

    def __str__(self):
        return self.user.username

    def reduce_wallet_sum(self, order_sum):
        self.profile_wallet = self.profile_wallet - order_sum
        return self.save()

    def add_wallet_sum(self, order_sum):
        self.profile_wallet = self.profile_wallet + order_sum
        return self.save()


class Item(models.Model):
    name = models.CharField(max_length=50)
    detail_info = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=17, decimal_places=2, null=True, blank=True,
                                validators=[MinValueValidator(Decimal('0.01'))])
    image = models.ImageField(null=True, blank=True)
    count_items = models.PositiveIntegerField(default=0)

    def reduce_item_count(self, count_of_items):
        self.count_items = self.count_items - count_of_items
        return self.save()

    def add_item_count(self, count_of_items):
        self.count_items = self.count_items + count_of_items
        return self.save()


class ShoppingEvent(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count_of_items = models.PositiveIntegerField(default=0)
    event_date_time = models.DateTimeField(auto_now_add=True,)
    order_sum = models.DecimalField(max_digits=17, decimal_places=2, null=True, blank=True,
                                    validators=[MinValueValidator(Decimal('0.01'))])

    def check_count_of_items(self):
        if self.count_of_items > self.item.count_items:
            return False  # raise ValidationError("Oops count of items more then we have")
        return True

    def check_sum_in_profile_wallet(self):
        if self.count_of_items * self.item.price > self.profile.profile_wallet:
            # raise ValidationError("Oops you sum in ypur wallet less than")
            return False
        return True


class ReversalEvent(models.Model):
    shopping_event = models.OneToOneField(ShoppingEvent, on_delete=models.CASCADE)
    event_date_time = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

