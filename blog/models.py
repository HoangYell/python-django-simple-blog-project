from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1000)
    date_publish = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:post_list')

    def publish_post(self):
        self.date_publish = timezone.now()
        self.save()
