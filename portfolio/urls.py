from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('<slug:slug>', views.project_details, name='project-details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('download-cv/', views.download_cv, name='download_cv'),
]
