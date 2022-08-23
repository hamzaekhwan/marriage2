from django.db import models

# Create your models here.
class inviteMarried_request(models.Model)    :
    fullName=models.CharField(max_length=200)
    titleName=models.CharField(max_length=200)
    date=models.DateField()
    male_picture = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    invite_picture= models.ImageField(null=True, blank=True,
                              default='/placeholder.png')            