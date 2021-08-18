import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'models_project_1.settings')

import django
django.setup() # --> Will configure.porjects settings

## fake population scripts
import random
from app_1.models import Topic,Webpage,AccessRecord
from faker import Faker

fakegen = Faker()  ## fakegen is a Faker() object
topics  = ['Search' , 'Social' , 'Marketplace' , 'News' , 'Games']

def add_topic():
    ## get_or_create() --> retrieve the topic if already exists/create it
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()   ## from the above topics pick one topic randomly

        ## create the fake data for each entry
        fake_url  = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        ## create new web-page entry
        webpg = Webpage.objects.get_or_create(topic=top , url=fake_url , name=fake_name)[0]

        ## create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg , date=fake_date)[0]
                                                ## foreign key purpose

if __name__ == '__main__':
    print("Populating Scripts")
    populate(20)  ## Specify how many dummy rows are required 
    print("Populating completed")


