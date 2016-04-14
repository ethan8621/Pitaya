from django.db import models

# database User table
class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    admin_privilege = models.BooleanField()
    user_password = models.CharField(max_length=200)

