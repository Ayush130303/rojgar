from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    tags = models.JSONField()
    url = models.URLField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Profile(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    profile_img=models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Savedpost(models.Model):
    jobid=models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='saved'
    )
    saved_at=models.DateField(auto_now_add=True)
    profile=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='saved_post'
    )

    def __str__(self):
        return f"{self.user.username} on {self.saved_at}"
