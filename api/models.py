from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length = 20,primary_key=True)
    real_name = models.CharField(max_length = 30)
    tz = models.CharField(max_length = 30)

    def __str__(self):
        return self.user_id

class ActivityPeriod(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now, blank=False)
    end_time = models.DateTimeField(default=datetime.now, blank=False)



    