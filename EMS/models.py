from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=120)
    location = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    description = models.TextField()

    class Meta:
        db_table = 'EMS_Event'  # Specify the table name as 'event'

    def __str__(self):
        return self.event_title

class Registration(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=35)
    ph_no = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        db_table = 'EMS_Registration'  # Specify the table name as 'registration'

    def __str__(self):
        return self.full_name
