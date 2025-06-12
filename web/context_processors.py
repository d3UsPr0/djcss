from .models import WeeklyProgram

def weekly_programs(request):
    return {
        'weekly_programs': WeeklyProgram.objects.all().order_by('display_order', 'day')
    }