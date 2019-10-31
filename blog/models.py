from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    overview = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_counter = models.IntegerField(default=0)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField()

    def __str__(self):
        return "Post object (id={} & title={})".format(self.id, self.title)
