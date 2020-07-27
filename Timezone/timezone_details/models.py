from django.db import models

from Country.models import Country
from Task_Type.models import Task_Type
from User.models import User
# Create your models here.

class Timezone_detail(models.Model):
    # id = models.IntegerField(primary_key=True)
    tasktype = models.ForeignKey(Task_Type, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # percentage = models.IntegerField()
    starttime=models.TimeField()
    endtime = models.TimeField()
    active = models.CharField(max_length=10, default='Y')


    class Meta:
        db_table = 'Timezone_detail'