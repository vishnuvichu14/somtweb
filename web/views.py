from django.shortcuts import render


def landing_page(request):
    return render(request, 'web/landing_page.html')
