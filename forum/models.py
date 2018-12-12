from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from propose_join.models import ExistingClub
#from registration.models import Profile
#from propose_join.models import Clubs

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    in_club = models.ForeignKey(ExistingClub, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True ,related_name='post_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

class Comments(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_to = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Replies(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
