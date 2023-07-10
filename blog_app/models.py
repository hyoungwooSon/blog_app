from django.db import models

# Create your models here.
class Post(models.Model):
    subject=models.CharField(max_length=50, blank=False)
    created_date=models.DateTimeField(null=True, blank=True)
    memo=models.CharField(max_length=200, blank=False)
    selectType=models.CharField(max_length=20, blank=False, default="Django")
    def __str__(self):
        return self.subject