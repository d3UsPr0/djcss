from django.contrib import admin
from django.utils.html import mark_safe
from .models import News, Prayer, Publication, SchoolStatistics, Staff, WeeklyProgram
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

# Register your models here.
class NewsAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False  # Optional: Avoid "This field is required" errors

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='default'
            ),
        }
        
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm  # Integrates CKEditor 5
    list_display = ('title', 'category', 'author', 'publish_date', 'is_published', 'is_featured')
    list_filter = ('category', 'is_published', 'is_featured')
    search_fields = ('title', 'excerpt', 'content')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)
        
class NewsAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = False  # Avoid "This field is required" errors

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'}, 
                config_name='default'
            ),
        }
    
@admin.register(WeeklyProgram)
class WeeklyProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'day', 'icon', 'icon_color', 'display_order')
    list_editable = ('display_order',)  # Allows inline editing of order
    list_filter = ('day',)
    search_fields = ('name', 'day')
    ordering = ('display_order', 'day')

@admin.register(SchoolStatistics)
class SchoolStatisticsAdmin(admin.ModelAdmin):
    list_display = ('year', 'teachers', 'form_one', 'form_two', 
                   'form_three', 'form_four', 'total_students', 'last_updated')
    readonly_fields = ('total_students', 'last_updated')
    list_editable = ('teachers', 'form_one', 'form_two', 'form_three', 'form_four')
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'display_order', 'photo_preview')
    list_editable = ('display_order',)
    list_filter = ('position',)
    search_fields = ('name', 'position', 'email')
    readonly_fields = ('photo_preview',)  # Make preview read-only
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'bio', 'display_order')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone'),
            'classes': ('collapse',)
        }),
        ('Social Media', {
            'fields': ('linkedin', 'twitter'),
            'classes': ('collapse',)
        }),
        ('Profile Image', {
            'fields': ('photo_preview', 'photo'),
            'description': 'Upload a square image (800x800px recommended)'
        })
    )

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 200px; max-width: 200px;" />')
        return "No photo uploaded"
    photo_preview.short_description = 'Current Photo'

@admin.register(Prayer)
class PrayerAdmin(admin.ModelAdmin):
    list_display = ('week_title', 'day', 'title', 'prayer_date')
    list_filter = ('day', 'prayer_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'prayer_date'
    
    fieldsets = (
        (None, {
            'fields': ('week_title', 'day', 'prayer_date')
        }),
        ('Content', {
            'fields': ('title', 'description', 'scripture_reference'),
        }),
    )

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_featured', 'date_uploaded', 'download_count')
    list_editable = ('is_published', 'is_featured')  # Quick toggle in list view
    list_filter = ('is_published', 'is_featured', 'date_uploaded')
    search_fields = ('title', 'subtitle')
    date_hierarchy = 'date_uploaded'

