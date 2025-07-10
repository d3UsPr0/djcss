from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinValueValidator

# web/models.py
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
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    name = models.CharField(max_length=100, help_text="E.g. Sports Day, Debate, etc.")
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

class SchoolStatistics(models.Model):
    YEAR_CHOICES = [(year, year) for year in range(2020, 2031)]
    
    year = models.PositiveIntegerField(
        choices=YEAR_CHOICES,
        default=timezone.now().year,
        unique=True
    )
    teachers = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    form_one = models.PositiveIntegerField(
        verbose_name="Form 1 Students",
        default=0,
        validators=[MinValueValidator(0)]
    )
    form_two = models.PositiveIntegerField(
        verbose_name="Form 2 Students",
        default=0,
        validators=[MinValueValidator(0)]
    )
    form_three = models.PositiveIntegerField(
        verbose_name="Form 3 Students",
        default=0,
        validators=[MinValueValidator(0)]
    )
    form_four = models.PositiveIntegerField(
        verbose_name="Form 4 Students",
        default=0,
        validators=[MinValueValidator(0)]
    )
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "School Statistics"
        ordering = ['-year']

    def __str__(self):
        return f"School Statistics - {self.year}"

    @property
    def total_students(self):
        return self.form_one + self.form_two + self.form_three + self.form_four

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['display_order', 'name']
        
    def __str__(self):
        return f"{self.name} - {self.position}"
    
class Prayer(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    
    week_title = models.CharField(max_length=100)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    scripture_reference = models.CharField(max_length=200, blank=True, null=True)
    prayer_date = models.DateField()
    
    class Meta:
        ordering = ['prayer_date']
    
    def __str__(self):
        return f"{self.week_title} - {self.day}"
    
    @classmethod
    def get_current_week_prayers(cls):
        today = timezone.now().date()
        start_week = today - timezone.timedelta(days=today.weekday())
        end_week = start_week + timezone.timedelta(days=6)
        return cls.objects.filter(prayer_date__range=[start_week, end_week])
class Publication(models.Model):
    # Core fields (required)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='publications/%Y/%m/%d/')
    date_uploaded = models.DateTimeField(default=timezone.now)
    
    # Publication control flags
    is_featured = models.BooleanField(default=False, 
        help_text="Mark as featured to highlight this publication")
    is_published = models.BooleanField(default=True,
        help_text="Uncheck to hide this publication from public view")
    
    # Automatic tracking
    download_count = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ['-date_uploaded']
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
        return self.title

    def increment_download_count(self):
        """Call this when file is downloaded"""
        self.download_count += 1
        self.save(update_fields=['download_count'])
    