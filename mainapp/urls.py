from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('start/', views.start_check, name='start'),
    path('api/site_check/', views.get_website)
]
