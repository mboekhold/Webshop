from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, )
    first_name = models.CharField(max_length=50, default='No First Name')
    last_name = models.CharField(max_length=50, default='No Last Name')
    description = models.TextField(default='No Description')
    quote = models.TextField(default='No Quote')

    def __str__(self):
        return f'{self.user.username} Profile'

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance,
                   created, **kwargs):
    print(Profile.objects.all())
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance,
                 **kwargs):
    instance.profile.save()
