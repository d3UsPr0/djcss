from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import GalleryImage, News, Prayer, Publication, Staff, SchoolStatistics, WeeklyProgram
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

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

def read_more(request):
    return render(request, 'web/welcome.html')

def bulletins(request):
    return render(request, 'web/news.html')

def events(request):
    return render(request, 'web/events.html')

def prayers(request):
    return render(request, 'web/prayers.html')

def videos(request):
    return render(request, 'web/videos.html')

def contact(request):
    return render(request, 'web/contacts.html')

def admissions(request):
    return render(request, 'web/admission.html')

def academics(request):
    return render(request, 'web/academics.html')

def gallery(request):
    return render(request, 'web/gallery.html')
def about(request):
    return render(request, 'web/about.html')

def publication_list(request):
    # Get featured publications first (published and featured)
    featured = Publication.objects.filter(
        is_published=True,
        is_featured=True
    ).order_by('-date_uploaded')
    
    # Then get regular published (non-featured) publications
    regular = Publication.objects.filter(
        is_published=True,
        is_featured=False
    ).order_by('-date_uploaded')
    
    # Combine both querysets (featured first)
    publications = list(featured) + list(regular)
    
    context = {
        'publications': publications,
        # 'global_bulletins': your_news_queryset,  # Keep existing context
    }
    return render(request, 'web/downloads.html', context)

@require_POST
def increment_download_count(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    publication.increment_download_count()
    return JsonResponse({'success': True, 'new_count': publication.download_count})

def gallery(request):
         # Get all images with featured ones first
    all_photos = GalleryImage.objects.all().order_by('-is_featured', '-upload_date')
    
    
    context = {
        
        'gallery_photos': all_photos,

    }

    return render(request, 'web/gallery.html', context)