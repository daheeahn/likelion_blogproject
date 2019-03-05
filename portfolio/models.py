from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/') # images라는 dir에 업로드할거다
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title