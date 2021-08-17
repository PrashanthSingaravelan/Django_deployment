from django.db import models

class Topic(models.Model):   ## Topic class inheriting from Model class via model  
    top_name = models.CharField(max_length=254 , unique=True)  
    # top_name --> field name
    # (unique=True) --> primary key

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    ## topic --> foreign key 
    ## Since top_name in Topic --> primary key

    name = models.CharField(max_length=254,unique=True)
    url  = models.URLField(unique=True)
    # name and url --> primary key

    def __str__(self):
        return self.name

class AccessRecord(models.Mode):
    name = models.ForeignKey(Webpage)
    ## name --> foreign key 
    ## Since name, url in Webpage --> primary key

    date = models.DateField()

    def __str__(self):
        return str(self.date)
