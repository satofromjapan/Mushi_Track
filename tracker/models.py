from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Mushi(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # assignee = models.SOMETHING
    # steps_to_repo = models.TextField()
    # expected_results = models.TextField()
    # actual results = models.TextField()
    # comments = models.ForeignKey()
    # keywords = models.CharField()
    # priority
    


    def __str__(self):
        return self.title
    
