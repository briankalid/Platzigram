from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Create your models here.

class Profile(AbstractUser):

    website = models.URLField(max_length=200,blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)

    picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #USERNAME_FIELD = 'phone_number'
    #REQUIRED_FIELDS = []
    #def __str__(self):
        #print(self.username)
