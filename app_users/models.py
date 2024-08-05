from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your models here.
import hashlib
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info =  models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
    
    def save(self,*args,**kwargs):
        if self.image:
            # Generate SHA-1 hash of the file content
            sha1 = hashlib.sha1(self.image.read()).hexdigest()
             # Preserve the file extension
            ext = os.path.splitext(self.image.name)[1]
            # Combine hash with extension to create new file name
            new_filename = f"{sha1}{ext}"
            print(new_filename)
            self.image.name = default_storage.save(f'avatars/{new_filename}', ContentFile(self.image.read()))
        super().save(*args, **kwargs)


    # @property
    # def name(self):
    #     if self.displayname:
    #         name = self.displayname
    #     else:
    #         name = self.user.username
    #     return name
    
    # @property
    # def avatar(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         avatar = self.image.url
    #     else:
    #         avatar = static('images/avatar.svg')
    #     return avatar

    @property
    def name(self):
            if self.displayname:
                return self.displayname
            return self.user.username 
        
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return static("images/avatar.svg")