from django.urls import path
from . import views

urlpatterns = [
    path('', views.Websites.as_view(), name='websites'),
    path('website/<int:pk>', views.WebsitesDetailView.as_view(), name='website-detail'),
    path('create_website/', views.CreateWebsite.as_view(), name='create-website'),
    path('create_webpage/', views.CreateWebPage.as_view(), name='create-webpage'),
    path('categories/', views.CategoriesList.as_view(), name='categories'),
    path('create_category/', views.CreateCategory.as_view(), name='create-category')
]
