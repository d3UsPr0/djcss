    
from django.shortcuts import render
from django.utils import timezone
from .models import News
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    # Get 3 latest featured news for main content
    featured_news = News.objects.filter(
        is_featured=True,
        is_published=True,
        publish_date__lte=timezone.now()
    ).order_by('-publish_date')[:3]
    
    # Get all news for bulletins (featured first, then others)
    bulletins = News.objects.filter(
        is_published=True,
        publish_date__lte=timezone.now()
    ).order_by('-is_featured', '-publish_date')  # Featured first (True > False)
    
    return render(request, 'web/home.html', {
        'featured_news': featured_news,
        'bulletins': bulletins
    })
    
def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    # Get 3 latest featured news for main content
    featured_news = News.objects.filter(
        is_featured=True,
        is_published=True,
        publish_date__lte=timezone.now()
    ).order_by('-publish_date')[:3]
    
    # Get all news for bulletins (featured first, then others)
    bulletins = News.objects.filter(
        is_published=True,
        publish_date__lte=timezone.now()
    ).order_by('-is_featured', '-publish_date')  # Featured first (True > False)
    return render(request, 'web/news_detail.html', {'news': news, 'featured_news': featured_news, 'bulletins': bulletins})