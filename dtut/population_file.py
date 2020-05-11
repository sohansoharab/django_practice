import os
import django
import random
from faker import Faker

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtut.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dtut.settings'
django.setup()
from frst_app.models import Topic, Webpage, AccessRecord
fakegen = Faker()
topics = ['Serach', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t=Topic.objects.get_or_create(Top_name = random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for i in range(n):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        wbpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        accs_rec = AccessRecord.objects.get_or_create(name=wbpg, date=fake_date)[0]


if __name__ == '__main__':
    populate(20)
    print('populating done')

