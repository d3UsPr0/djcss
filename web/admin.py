from django.contrib import admin
from .models import News, SchoolStatistics, WeeklyProgram

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
