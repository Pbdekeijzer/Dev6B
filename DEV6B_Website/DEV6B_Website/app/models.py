"""
Definition of models.
"""

from django.db import models

class DataBaseUser(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class GameUser(models.Model):
    username = models.OneToOneField(DataBaseUser, primary_key=True)
    cash = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.username

class Jobs(models.Model):
    jobname = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100)
    expreward = models.PositiveIntegerField()

    def __str__(self):
        return self.jobname

class DoneJobs(models.Model):
    jobname = models.ForeignKey(Jobs)
    username = models.ForeignKey(GameUser)

    def __str__(self):
        return self.jobname, self.username