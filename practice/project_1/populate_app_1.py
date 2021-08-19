import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'project_1.settings')

import django
django.setup() # --> Will configure.porjects settings

## fake population scripts
import random
from app_1.models import users
from faker import Faker

fakegen = Faker()  ## fakegen is a Faker() object

def populate(N=5):
    for entry in range(N):

        ## create the fake data for each entry
        fake_name = fakegen.name().split()
        fake_first_name     = fake_name[0]
        fake_last_name      = fake_name[1]
        fake_mail_address   = fakegen.email()

        ## create new users entry
        user = users.objects.get_or_create(first_name=fake_first_name , 
            last_name=fake_last_name , email=fake_mail_address)[0]

        
if __name__ == '__main__':
    print("Populating Scripts")
    populate(20)  ## Specify how many dummy rows are required
    print("Populating completed")
