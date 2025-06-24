from django.shortcuts import render
from django.utils import timezone
from .models import News, Staff, SchoolStatistics, WeeklyProgram
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'web/home.html')

def news_detail(request, slug):
    # Only need to pass news-specific data
    news = get_object_or_404(News, slug=slug, is_published=True)
    
    # You can still add view-specific context if needed
    context = {
        'news': news,
        # Add any additional view-specific variables here
        'related_news': News.objects.filter(
            is_published=True
        ).exclude(slug=slug).order_by('-publish_date')[:3]
    }
    return render(request, 'web/news_detail.html', context)

def staff(request):
    return render(request, 'web/staff.html', {
        'staff': Staff.objects.all()
    })

