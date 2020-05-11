import os
from faker import Faker
os.environ['DJANGO_SETTINGS_MODULE']='third_pro.settings'

import django
django.setup()

from third_app.models import UserPage, Indexes

fake_user = Faker()

def populate(n=10):
    for i in range(n):
        fake_frst_name = fake_user.name()
        fake_last_name = fake_user.name()
        fak_email = fake_user.email()
        user_info = UserPage.objects.get_or_create(frst_name=fake_frst_name, last_name=fake_last_name, email=fak_email)[0]
        user_index = Indexes.objects.get_or_create(frst_name=user_info)[0]
        user_info.save()
        user_index.save()

if __name__ == '__main__':
    populate(20)
    print("Population done!")