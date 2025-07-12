# web/context_processors.py
from django.utils import timezone
from django.db.models import Q
from .models import GalleryImage, News, Prayer, WeeklyProgram, SchoolStatistics

def global_context(request):
    """Makes these variables available in all templates"""
    # Get 3 latest events
    featured_news = News.objects.filter(
    is_published=True,  # Must be published
    publish_date__lte=timezone.now(),
    category="events"  # Only include events category
    ).exclude(
    ).order_by(
    '-is_featured',  # Featured items first (True comes before False)
    '-publish_date'   # Then sort by newest first
    )[:3]  # Adjust limit as needed
    

    
    # Get all news for bulletins
    bulletins = News.objects.filter(
        is_published=True,
        publish_date__lte=timezone.now()
    ).exclude(
    category="events"  # Exclude this category
    ).order_by('-is_featured', '-publish_date')
    
    # Get weekly programs
    weekly_programs = WeeklyProgram.objects.all().order_by('display_order', 'day')
    
    # Get school statistics
    current_year = timezone.now().year
    school_stats = SchoolStatistics.objects.filter(year=current_year).first()
    if not school_stats:
        school_stats = SchoolStatistics.objects.create(year=current_year)
        
    prayers = Prayer.get_current_week_prayers()
    current_week_title = prayers[0].week_title if prayers.exists() else ""
    
          # Get all images with featured ones first
    all_photos = GalleryImage.objects.filter(is_featured=False).order_by('-upload_date')
    
    # Separate featured photos for carousel
    featured_photos = GalleryImage.objects.filter(is_featured=True)
    
    
     
    return {
        'global_featured_news': featured_news,
        'global_bulletins': bulletins,
        'global_weekly_programs': weekly_programs,
        'global_school_stats': school_stats,
        'global_current_year': current_year,
        'prayers': prayers,
        'current_week_title': current_week_title,
        'featured_photos': featured_photos,
        'gallery_photos': all_photos,
        'has_featured': featured_photos.exists()
    }
    
