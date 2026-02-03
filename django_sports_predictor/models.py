import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Sport(models.Model):
    objects = None
    sport_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display(

        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    # Returns the actual question text, instead of the id
    def __str__(self):
        return f"({self.id}) {self.sport_text}"

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Returns the actual choice text, instead of the id
    def __str__(self):
        return self.choice_text
