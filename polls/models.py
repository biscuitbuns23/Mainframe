from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

class Appellation(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Ranking(models.Model):
    name = models.CharField(db_index=True, max_length=200)
    initials = models.CharField(db_index=True, max_length=10, blank=True, null=True)
    appellation = models.ManyToManyField(Appellation)

    def __str__(self):
        return f"{self.name}"

class Region(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"