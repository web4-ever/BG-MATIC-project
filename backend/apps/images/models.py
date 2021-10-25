from django.db import models
from django.db.models.fields import CharField
from apps.tags.models import Tag
from cloudinary.models import CloudinaryField

# Create your models here.# 
class Images(models.Model):
    class Meta(object):
        db_table = 'Images'

    name = models.CharField('Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous')
    description = models.CharField('Description', blank=False, null=False, max_length=500, db_index=True, default='Anonymous')
    image = CloudinaryField('image', blank=False, null=True)
    created_at = models.DateTimeField('Created Datetime', blank=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated Datetime', blank=False, auto_now_add=True)
    tags = models.ManyToManyField(
            Tag
        )

        