from django.db import models

# Create your models here.
class Tag(models.Model):
    class Meta(object):
        db_table = 'tag'
    
    name = models.CharField(
        'Name', blank=False, null=False, max_length=20, db_index= True
        )
    created_at = models.DateTimeField(
        'Created Datetime', blank=False, auto_now_add=True
        )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=False, auto_now_add=True
        )