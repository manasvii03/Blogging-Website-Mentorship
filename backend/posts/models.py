from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    summary = models.TextField(max_length=500, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    likes = models.ManyToManyField(User, related_name="liked_blogs", blank=True)
    stars = models.ManyToManyField(User, related_name="starred_blogs", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarked_blogs", blank=True)

    CATEGORY_CHOICES = [
        ('Culture', 'Culture'), ('Travel', 'Travel'), ('Food', 'Food'),
        ('Business', 'Business'), ('Tech', 'Tech'), ('Life', 'Life'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Life')
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def read_time(self):
        word_count = len(self.content.split())
        return max(1, round(word_count / 50))

    def __str__(self):
        return self.title