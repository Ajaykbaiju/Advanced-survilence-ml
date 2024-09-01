from django.db import models
from django.utils import timezone
from datetime import datetime, time

class station_regtable(models.Model):
    st_name=models.CharField(max_length=150)
    st_id=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class cam1tbl(models.Model):
    image=models.FileField(max_length=150)

class cam2tbl(models.Model):
    image=models.FileField(max_length=150)

class cam3tbl(models.Model):
    image=models.FileField(max_length=150)


    
   