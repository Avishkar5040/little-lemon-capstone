from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'


# Alias MenuItem to Menu
MenuItem = Menu


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} : {self.no_of_guests} guests on {self.booking_date}'

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
