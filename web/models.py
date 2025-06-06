from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class News(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic Updates'),
        ('exams', 'Examinations & Results'),
        ('events', 'Events & Celebrations'),
        ('sports', 'Sports & Games'),
        ('achievements', 'Student Achievements'),
        ('meetings', 'School Meetings'),
        ('holidays', 'Holidays & Schedules'),
        ('fees', 'Fee & Payment'),
        ('health', 'Health & Safety'),
        ('ict', 'ICT & e-Learning'),
        ('workshops', 'Workshops & Seminars'),
        ('competitions', 'Competitions'),
    ]

    title = models.CharField(max_length=255)
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    attachment = models.FileField(upload_to='news_attachments/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-publish_date']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title