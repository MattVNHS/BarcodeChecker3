from django.shortcuts import render

def home_screen_view(request):
    context = {}
    return render(request, 'homepage/home.html', context)
