from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    
    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
        
        class Meta:
            ordering = ('-created')
            index_together = (('id', 'slug'),)

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((450, 400))
        image = im
        # after modifications, save it to the output
        im.save(output, format='PNG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField',
                                          "%s.png" % self.image.name.split('.')[0],
                                          'image/png',
                                          sys.getsizeof(output), None)

        # pixelating image
        output = BytesIO()
        pixelSize = 4
        image = image.resize((int(450 / pixelSize), int(400 / pixelSize)), Image.NEAREST)
        image = image.resize((image.size[0] * pixelSize, image.size[1] * pixelSize), Image.NEAREST)
        image.save(output, format='PNG', quality=100)
        output.seek(0)
        self.image_pxl = InMemoryUploadedFile(output, 'ImageField',
                                              "%s.png" % self.image_pxl.name.split('.')[0],
                                              'image/png',
                                              sys.getsizeof(output), None)

        super(Product, self).save()
