from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title