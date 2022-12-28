from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
 
class Post(models.Model):
   class Meta(object):
       db_table = 'post'
      
   name = models.CharField(
       'name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
   )
  
   body = models.CharField(
       'body', blank=True, null=True, max_length=140, db_index=True
   )
  
   created_at = models.DateTimeField(
       'created_at', blank=True, auto_now_add=True
   )
   like = models.PositiveIntegerField(
    'like', default = 0, blank=True
   )
   image = CloudinaryField(
    'image', blank=True, null=True
   )
   updated_at = models.DateTimeField(
    'updated_at', blank=True, auto_now = True
   )


