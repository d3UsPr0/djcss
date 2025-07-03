from django.contrib import admin
from django.utils.html import mark_safe
from .models import News, Prayer, SchoolStatistics, Staff, WeeklyProgram

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'publish_date', 'is_published', 'is_featured')
    list_filter = ('category', 'is_published', 'is_featured')
    search_fields = ('title', 'excerpt', 'content')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)
    
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
            'fields': ('title', 'description')
        }),
    )