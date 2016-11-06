from django.db import models
from django.utils import timezone

class Post(models.Model):
    # author = models.ForeignKey(auth.User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pubished_date = timezone.now
        self.safe()

    def __str__(self):
        return self.title
