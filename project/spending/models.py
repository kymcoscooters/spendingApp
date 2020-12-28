from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    ssn = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nameStyle = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Receipt(models.Model):
    totalSum = models.DecimalField(decimal_places=2, max_digits=10)
    receiptDate = models.DateField('receipt date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.totalSum)
