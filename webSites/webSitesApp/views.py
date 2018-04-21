from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Website, WebPage, WebsiteCategory
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from .forms import CategoryForm


# class Websites(viewsets.ModelViewSet):
#     queryset = Website.objects.all()
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     filter_fields = ('category')
#     ordering = ('title')

class Websites(ListView):
    model = Website
    template_name = "websites.html"

    def get_queryset(self):
        if "category" in self.kwargs:
            category = WebsiteCategory.objects.filter(name=self.kwargs['category'])[0]
            return Website.objects.filter(category=category)
        if "ordering" in self.kwargs:
            return Website.objects.all().order_by(self.kwargs['ordering'])
        else:
            return Website.objects.all()


# class Websites(ListView):
#     model = Website
#     template_name = "websites.html"
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['title', 'category']
#
#     # def get_context_data(self, **kwargs):
#     #     website_list = Website.objects.all()
#     #     categories = WebsiteCategory.objects.all()
#     #     context = {
#     #         'website_list': website_list,
#     #         'categories': categories,
#     #     }
#     #     return context
#
#     def get_queryset(self, *args, **kwargs):
#         queryset_list = Website.objects.all()
#         query = self.request.GET.get("q")
#         if query:
#             queryset_list = queryset_list.filter(
#                 Q(category=query)).distinct()
#         return queryset_list
#
#     # def get_queryset(self):
#     #     category = WebsiteCategory.objects.filter(id=1)[0]
#     #     return Website.objects.filter(category=category)


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
