from django.db import models
from django.contrib.auth.models import User

class DropObjet(models.Model): # useless
    #user=models.ForeignKey(User)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def get_path(self):
        return '/' + self.user.username + '/' + self.name.replace('_', ' ')+'/'
# Create your models here.
