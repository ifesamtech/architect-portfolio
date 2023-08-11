from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


class ContactMessage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    

class Cv(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='cv/')

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    image = models.ImageField(null=False, blank=False, upload_to='project/image/')
    description = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
