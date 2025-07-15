from django.db import models,User

class Job(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    tags = models.JSONField()
    url = models.URLField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class profile(models.Model):
    jobid=models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_query_name='external_id'
    )
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='username'
    )
    profile_img=models.ImageField(type='jpg')
    saved_at=models.DateField(auto_now_add=True)