
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):

    titles=models.CharField(max_length=100)
    desc=models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.titles

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pro_pic=models.ImageField(upload_to='profile',default='download.png')
    bio=models.TextField(blank=True,null=True)
    dob = models.DateField(blank=True, null=True)
    prof = models.CharField(max_length=100, blank=True, null=True)
    qualif = models.CharField(max_length=100, blank=True, null=True)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
  



