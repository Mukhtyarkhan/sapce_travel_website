from django.shortcuts import render, redirect


def home_page(request):
   return render(request, 'index.html')


def design_system(request):
    return render(request, 'design-system.html')

def destination_moon(request):
    return render(request, 'destination-moon.html')
 
def crew_recommender(request):
    return render(request, 'crew-commender.html')
