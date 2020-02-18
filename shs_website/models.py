from django.db import models

# Create your models here.


# Create your models here.
class EventDetail(models.Model):
    EventName = models.CharField(max_length=10000)
    EventDate = models.DateField()

    def __str__(self):
        return str(self.EventDate)

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Body = models.CharField(max_length=10000)
    Images = models.FileField(upload_to='pics', null=True, blank=True)

class AddFacultyModel(models.Model):
    StaffName = models.CharField(max_length=1000)
    StaffQualification = models.CharField(max_length=5000)
    Subject = models.CharField(max_length=1000)

class NotificationsModel(models.Model):
    notifications = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.notifications)





