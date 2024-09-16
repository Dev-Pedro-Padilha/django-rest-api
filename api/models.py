from django.db import models


def upload_image_task(instance, filename):
    return f"{instance.id}-{filename}"

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.content

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_task, blank=True, null=True)
    
    def __str__(self):
        return self.title