from django.shortcuts import render, get_object_or_404
from .models import Page

COUNTRY_NAME = "North Korea (Democratic People's Republic of Korea)"

def menu_pages():
    # Shows all pages that exist in the DB (so Flag appears when you add it)
    return Page.objects.order_by("id")

def home(request):
    page = get_object_or_404(Page, slug="home")
    return render(request, "pages/home.html", {
        "country": COUNTRY_NAME,
        "page_title": "Home",
        "page_meta": page,
        "menu": menu_pages(),
    })

def history(request):
    page = get_object_or_404(Page, slug="history")
    return render(request, "pages/history.html", {
        "country": COUNTRY_NAME,
        "page_title": "History",
        "page_meta": page,
        "menu": menu_pages(),
    })

def languages(request):
    page = get_object_or_404(Page, slug="languages")
    return render(request, "pages/languages.html", {
        "country": COUNTRY_NAME,
        "page_title": "Language(s)",
        "page_meta": page,
        "menu": menu_pages(),
    })

def references(request):
    page = get_object_or_404(Page, slug="references")
    return render(request, "pages/references.html", {
        "country": COUNTRY_NAME,
        "page_title": "References",
        "page_meta": page,
        "menu": menu_pages(),
    })

def flag(request):
    page = get_object_or_404(Page, slug="flag")
    return render(request, "pages/flag.html", {
        "country": COUNTRY_NAME,
        "page_title": "Flag",
        "page_meta": page,
        "menu": menu_pages(),
    })





