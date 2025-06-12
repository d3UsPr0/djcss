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

class WeeklyProgram(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    ICON_CHOICES = [
        ('fas fa-running', 'Sports'),
        ('fas fa-comments', 'Debate'),
        ('fas fa-broom', 'Cleanliness'),
        ('fas fa-leaf', 'Shamba'),
        ('fas fa-praying-hands', 'Service & Prayer'),
        ('fas fa-trophy', 'Weekend Challenge'),
        ('fas fa-users', 'School Baraza'),
        ('fas fa-handshake', 'Parent-Teacher Meeting'),
        ('fas fa-door-open', 'Welcoming Guests'),
        ('fas fa-music', 'Entertainment'),
    ]
    
    ICON_COLORS = [
        ('text-primary', 'Blue'),
        ('text-success', 'Green'),
        ('text-danger', 'Red'),
        ('text-warning', 'Yellow'),
        ('text-info', 'Cyan'),
        ('text-secondary', 'Gray'),
        ('text-dark', 'Black'),
    ]
    
    icon_color = models.CharField(
        max_length=20,
        choices=ICON_COLORS,
        default='text-primary',
        help_text="Color for the program icon"
    )
    
    name = models.CharField(max_length=100, help_text="E.g. Sports Day, Debate, etc.")
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fas fa-calendar-day')
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'day']
        verbose_name = "Weekly Program"
        verbose_name_plural = "Weekly Programs"
        
    def save(self, *args, **kwargs):
        # Auto-set display order based on day
        day_order = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 
                    'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
        self.display_order = day_order.get(self.day, 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.day}: {self.name}"