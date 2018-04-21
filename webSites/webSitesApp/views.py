from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Website, WebPage, WebsiteCategory
from django.db.models import Q
from django.urls import reverse_lazy


class Websites(ListView):
    # TODO Sorting + filtering together, sessions?
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
    initial = {'date_added': '2018-04-21', 'date_updated': '2018-04-21'}
    template_name = "website_create.html"
    success_url = reverse_lazy('websites')


class CreateWebPage(CreateView):
    model = WebPage
    fields = '__all__'
    initial = {'date_added': '2018-04-21', 'date_updated': '2018-04-21'}
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
    initial = {'date_added': '2018-04-21', 'date_updated': '2018-04-21'}
    template_name = "category_create.html"
    success_url = reverse_lazy('categories')
