# web/context_processors.py
from django.utils import timezone
from .models import News, WeeklyProgram, SchoolStatistics

def global_context(request):
    """Makes these variables available in all templates"""
    # Get 3 latest featured news
    featured_news = News.objects.filter(
        is_featured=True,
        is_published=True,
        publish_date__lte=timezone.now()
    ).order_by('-publish_date')[:3]
    
    # Get all news for bulletins
    bulletins = News.objects.filter(
        is_published=True,
        publish_date__lte=timezone.now()
    ).order_by('-is_featured', '-publish_date')
    
    # Get weekly programs
    weekly_programs = WeeklyProgram.objects.all().order_by('display_order', 'day')
    
    # Get school statistics
    current_year = timezone.now().year
    school_stats = SchoolStatistics.objects.filter(year=current_year).first()
    if not school_stats:
        school_stats = SchoolStatistics.objects.create(year=current_year)
    
    return {
        'global_featured_news': featured_news,
        'global_bulletins': bulletins,
        'global_weekly_programs': weekly_programs,
        'global_school_stats': school_stats,
        'global_current_year': current_year
    }