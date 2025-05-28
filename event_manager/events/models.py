from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=150)

    def __str__(self):
        return f'Event - {self.title}  {self.date}'