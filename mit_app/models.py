from django.db import models
import datetime

class Mitnadv(models.Model):
    
    GENDER = (
        ("M","Male"),
        ("F","Female")
    )

    f_name = models.CharField(max_length = 30)
    l_name = models.CharField(max_length = 30, blank = True, null=True)
    gander = models.CharField(max_length = 1,choices = GENDER, blank = True, null=True)
    age = models.CharField(max_length = 30, blank = True, null=True)

    address = models.CharField(max_length = 100, blank = True, null=True)
    phone = models.CharField(max_length = 100, blank = True, null=True)
    email = models.EmailField(blank = True, null=True)
    image = models.ImageField(upload_to = "upload/" ,blank = True, null=True) 

    snif = models.ForeignKey("Snif", on_delete=models.SET_NULL, null= True)

    money_for_month = models.CharField(max_length = 4)

    time_start = models.TimeField(blank = True, null =True)
    time_end = models.TimeField(blank = True, null =True)

    def __str__(self):
        return self.f_name

    @property
    def new_price(self, input_m=4):

        money_m =int(self.money_m)
        input_m =int(input_m)

        newprice = money_m * input_m
        return self.newprice

    
    
class Snif(models.Model):
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 20)
    image = models.ImageField(upload_to = "upload/",blank = True, null = True)

    def __str__(self):
        return self.name

class PayForMounthModel(models.Model):
    
 #   pay_m = models.CharField(blank = True, null = True)

    to = models.OneToOneField(Mitnadv ,on_delete=models.SET_NULL , blank = True, null = True)
    total = models.CharField(max_length = 10,blank = True, null = True)

    def __str__(self):
        return self.pay_m.f_name
    