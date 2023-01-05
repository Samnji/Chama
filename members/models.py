from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    deposit_amount = models.IntegerField()
    withdraw_amount = models.IntegerField()
    rank = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
