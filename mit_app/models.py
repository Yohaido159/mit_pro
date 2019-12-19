from django.db import models
import datetime

class Gift(models.Model):
    gift = models.CharField(max_length = 30)
    use = models.BooleanField(default=False)

    def __str__(self):
        return self.gift

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

    gifts = models.ManyToManyField(Gift)
    

    def __str__(self):
        return self.f_name
    
    
class Snif(models.Model):
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 20)
    image = models.ImageField(upload_to = "upload/",blank = True, null = True)

    def __str__(self):
        return self.name




#    GIFTS = [
#        ("TE","teeth"),
#        ("VE","vacation"),
#        ("CL","clothes"),
#        ("CO","course"),
#    ]
#
#    gift = models.CharField(max_length = 2, choices = GIFTS, default = "CL")
