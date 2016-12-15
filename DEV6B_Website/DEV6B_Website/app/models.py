"""
Definition of models.
"""

from django.db import models
import Database

# Create your models here.
def GetGameUserData(username):
    Query = "SELECT * FROM Game_User"# WHERE Name = '{0}'".format(str(username))
    print(Query)
    result = Database.Execute_Query(Query)
    print(result)

GetGameUserData('username')