from django.core.management.base import BaseCommand
from api.models import User , ActivityPeriod
from datetime import datetime, timedelta
from django.utils import timezone
from faker import Faker

faker = Faker()	

class Command(BaseCommand):
    help = 'Create random users and ActivityPeriod'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users and activity to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
        	try:
        		user_id=faker.md5()[::4].upper()
        		User.objects.create(user_id=user_id,real_name=faker.name(),tz=faker.timezone())

        		ac=faker.random_int(1,5)
        		
        		for j in range(ac):
        			start_time=faker.date_time()
        			ActivityPeriod.objects.create(User_id=user_id,start_time=start_time, end_time=start_time+timedelta(hours=1))

        		#self.stdout.write("%s Activity created succesfully" % ac)


        	except:
        		pass

        self.stdout.write("%s fakedataset created succesfully" % total)