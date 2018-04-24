from django.views.generic import ListView, DetailView, CreateView
from .models import Website, WebPage, WebsiteCategory
from django.urls import reverse_lazy
import datetime
from webSites.tasks import *


class Websites(ListView):
    model = Website
    template_name = "websites.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        categories = WebsiteCategory.objects.all()
        data['categories'] = categories
        field_names = ['url', 'title', 'date_added', 'date_updated']
        data['field_names'] = field_names
        return data

    def get_queryset(self):
        if "category" in self.kwargs:
            category = WebsiteCategory.objects.filter(name=self.kwargs['category'])[0]
            self.request.session['category'] = category.name
            return Website.objects.filter(category=category)
        if "ordering" in self.kwargs:
            if self.request.session['category'] == "all":
                return Website.objects.all().order_by(self.kwargs['ordering'])
            else:
                category_name = self.request.session['category']
                category = WebsiteCategory.objects.filter(name=category_name)[0]
                return Website.objects.filter(category=category).order_by(self.kwargs['ordering'])
        else:
            self.request.session['category'] = "all"
            return Website.objects.all()[:10]


class WebsitesDetailView(DetailView):
    model = Website
    template_name = "website_detail.html"


class CreateWebsite(CreateView):
    model = Website
    fields = '__all__'
    now = datetime.datetime.now()
    today = "{}-{}-{}".format(now.year, now.month, now.day)
    initial = {'date_added': today, 'date_updated': today}
    template_name = "website_create.html"
    success_url = reverse_lazy('websites')


class CreateWebPage(CreateView):
    model = WebPage
    fields = '__all__'
    now = datetime.datetime.now()
    today = "{}-{}-{}".format(now.year, now.month, now.day)
    initial = {'date_added': today, 'date_updated': today}
    template_name = "webpage_create.html"
    success_url = reverse_lazy('websites')


class CategoriesList(ListView):
    model = WebsiteCategory
    template_name = "website_category.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        self.get_count()
        return data

    @staticmethod
    def get_count():
        categories = WebsiteCategory.objects.all()
        for category in categories:
            count = Website.objects.filter(category=category).count()
            category.count = count
            category.save()


class CreateCategory(CreateView):
    model = WebsiteCategory
    fields = '__all__'
    now = datetime.datetime.now()
    today = "{}-{}-{}".format(now.year, now.month, now.day)
    initial = {'date_added': today, 'date_updated': today}
    template_name = "category_create.html"
    success_url = reverse_lazy('categories')


class DownloadWebsites(ListView):
    template_name = "download_websites.html"
    model = Website

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
        out_path = "webSitesApp/static/"
        result = download_file.delay(url, out_path)
        #result = download_file.apply_async(url)
        return data
