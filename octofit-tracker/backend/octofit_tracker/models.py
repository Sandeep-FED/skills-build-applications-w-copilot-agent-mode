from django.db import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()