from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps, ImageDraw
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def save(self, **kwargs):
        # Opening the uploaded image

        if self.image:
            print(self.image)
            super().save()
            print("hello")
            im = Image.open(self.image)

            output = BytesIO()

            # Resize/modify the image
            im = im.resize((450, 400))

            # after modifications, save it to the output
            im.save(output, format='PNG', quality=100)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField',
                                              "%s.png" % self.image.name.split('.')[0],
                                              'image/png',
                                              sys.getsizeof(output), None)

            image = Image.open(self.image)
            bigsize = (image.size[0] * 3, image.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(im.size, Image.ANTIALIAS)
            im.putalpha(mask)

            circle_image = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
            circle_image.putalpha(mask)
            output = BytesIO()
            circle_image.save(output, format='PNG', quality=100)
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField',
                                              "%s.png" % self.image.name.split('.')[0],
                                              'image/png',
                                              sys.getsizeof(output), None)
        else:
            super().save()


@receiver(post_save, sender=User)
def create_profile(sender, instance,
                   created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance,
                 **kwargs):
    instance.profile.save()
