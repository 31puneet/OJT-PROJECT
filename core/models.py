from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('draft', 'Drafts/Notes'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page_covers/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    # Who created the page?
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages_created')
    
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PageVersion(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='versions')
    content = models.TextField()
    cover_image = models.ImageField(upload_to='version_covers/', blank=True, null=True)
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    
    # Who made this specific version?
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)