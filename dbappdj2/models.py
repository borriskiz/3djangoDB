from django.db import models


class ItemType(models.Model):
    name = models.CharField(verbose_name="Type name", max_length=255)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(verbose_name="Material name",max_length=100)
    dealer = models.ForeignKey("Dealer", on_delete=models.CASCADE)
    cost = models.IntegerField()

    def __str__(self):
        return self.name


class Dealer(models.Model):
    name = models.CharField(verbose_name="Dealer name",max_length=100)
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(verbose_name="Market name",max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class HandmadeItem(models.Model):
    name = models.CharField(verbose_name="Item name",max_length=200)
    date_receipt = models.DateField(verbose_name="date of receipt")
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name