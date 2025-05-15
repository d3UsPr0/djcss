from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'DJCSS | Home',
    }
    return render(request,'web/home.html',context)