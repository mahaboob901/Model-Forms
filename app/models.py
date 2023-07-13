from tkinter import Widget
from django.db import models

# Create your models here.
class  Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.Topic_name

class WebPage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self) -> str:
        return self.name


class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.author
    

    

