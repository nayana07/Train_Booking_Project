from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.


class train(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    train_no = models.CharField(max_length=50,blank=True)
    train_from = models.CharField(max_length=50,blank=True)
    dep_time = models.CharField(max_length=50, blank=True)
    train_to = models.CharField(max_length=50,blank=True)
    arr_time = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.train_no

    def __iter__(self):
        for no,field_name in enumerate(self._meta.get_fields()):
            if int(no) == 0:
                last = str(field_name).split('.')[-1][:-1]
            else:
                last = str(field_name).split('.')[-1]
            value = getattr(self, last, None)
            yield (field_name, value)

class booking(models.Model):
    t_id = models.ForeignKey(
        train,
        on_delete=models.CASCADE,
    )
    booking_seats = models.IntegerField(blank=True)
    booking_class = models.CharField(max_length=10,blank=True)
    ph_no = models.IntegerField(blank=True)
    name1 = models.CharField(max_length=50,blank=True, null=True)
    nationality1 = models.CharField(max_length=50,blank=True)
    gender1 = models.CharField(max_length=50,blank=True, null=True)
    age1 = models.IntegerField(blank=True, null=True)
    name2 = models.CharField(max_length=50,blank=True, null=True)
    nationality2 = models.CharField(max_length=50,blank=True, null=True)
    gender2 = models.CharField(max_length=50,blank=True, null=True)
    age2 = models.IntegerField(blank=True, null=True)
    name3 = models.CharField(max_length=50,blank=True, null=True)
    nationality3 = models.CharField(max_length=50,blank=True, null=True)
    gender3 = models.CharField(max_length=50,blank=True, null=True)
    age3 = models.IntegerField(blank=True, null=True)
    name4 = models.CharField(max_length=50,blank=True, null=True)
    nationality4 = models.CharField(max_length=50,blank=True, null=True)
    gender4 = models.CharField(max_length=50,blank=True, null=True)
    age4 = models.IntegerField(blank=True, null=True)
    name5 = models.CharField(max_length=50,blank=True, null=True)
    nationality5 = models.CharField(max_length=50,blank=True, null=True)
    gender5 = models.CharField(max_length=50,blank=True, null=True)
    age5 = models.IntegerField(blank=True, null=True)
    name6 = models.CharField(max_length=100,blank=True, null=True)
    nationality6 = models.CharField(max_length=50,blank=True, null=True)
    gender6 = models.CharField(max_length=50,blank=True, null=True)
    age6 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name1

    def __iter__(self):
        for no,field_name in enumerate(self._meta.get_fields()):
            if int(no) == 0:
                last = str(field_name).split('.')[-1][:-1]
            else:
                last = str(field_name).split('.')[-1]
            value = getattr(self, last, None)
            yield (field_name, value)           



# Create your models here.
