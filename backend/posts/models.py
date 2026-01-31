from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    """
    FRONTEND NOTE:
    - Tags are dynamic (e.g.#LifeHacks).
    - You will receive these as a list of strings: ["tech"]
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # FRONTEND NOTE: Interaction Counters
    # You won't edit these directly. Use the /like/, /star/, /bookmark/ endpoints.
    likes = models.ManyToManyField(User, related_name="liked_blogs", blank=True)
    stars = models.ManyToManyField(User, related_name="starred_blogs", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarked_blogs", blank=True)

    # FRONTEND NOTE: Category Options
    # These are the EXACT strings you must send in your POST request.
    # These should match the buttons in your "Recommended Topics" sidebar.
    CATEGORY_CHOICES = [
        ('Culture', 'Culture'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Business', 'Business'),
        ('Tech', 'Tech'),
        ('Life', 'Life'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Life')

    # FRONTEND NOTE: Tags
    # Linked to the Tag model above.
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def read_time(self):
        # FRONTEND NOTE: 
        # This is auto-calculated. You don't need to send it.
        # Returns an integer (e.g. 5 means 5 min read).
        wpm = 200
        word_count = len(self.content.split())
        return max(1, round(word_count / 50))

    def __str__(self):
        return self.title