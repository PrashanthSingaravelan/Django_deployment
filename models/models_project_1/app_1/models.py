from django.db import models

class Topic(models.Model):   ## Topic class inheriting from Model class via model  
    top_name = models.CharField(max_length=254 , unique=True)  
    # top_name --> field name
    # (unique=True) --> primary key

    def _str_(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.DO_NOTHING)
    ## topic --> foreign key 
    ## Since top_name in Topic --> primary key

    name = models.CharField(max_length=254,unique=True)
    url  = models.URLField(unique=True)
    # name and url --> primary key

    def _str_(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.DO_NOTHING)
    ## name --> foreign key 
    ## Since name, url in Webpage --> primary key

    date = models.DateField()

    def _str_(self):
        return str(self.date)


