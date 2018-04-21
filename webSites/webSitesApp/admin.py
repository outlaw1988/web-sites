from django.contrib import admin
from .models import Website, WebPage, WebsiteCategory

# Register your models here.


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'meta_description')


@admin.register(WebPage)
class WebPageAdmin(admin.ModelAdmin):
    list_display = ('website', 'date_added', 'date_updated')


@admin.register(WebsiteCategory)
class WebsiteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
