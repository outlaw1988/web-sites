from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Website, WebPage, WebsiteCategory


class Websites(ListView):
    model = Website
    template_name = "websites.html"


class WebsitesDetailView(DetailView):
    model = Website
    template_name = "website_detail.html"


class CreateWebsite(CreateView):
    model = Website
    fields = '__all__'
    template_name = "website_create.html"


class CreateWebPage(CreateView):
    model = WebPage
    fields = '__all__'
    template_name = "webpage_create.html"


class CategoriesList(ListView):
    model = WebsiteCategory
    template_name = "website_category.html"


class CreateCategory(CreateView):
    model = WebsiteCategory
    fields = '__all__'
    template_name = "category_create.html"
