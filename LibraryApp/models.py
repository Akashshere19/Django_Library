from django.db import models
from datetime import date
# Create your models here.
class BookRecord(models.Model):
    BookName=models.CharField(max_length=100)
    OutDate=models.DateField()
    InDate=models.DateField()
    UserName=models.CharField(max_length=50,unique=True)
    MobNo=models.BigIntegerField()
