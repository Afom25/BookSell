from django.urls import path

from . import views

urlpatterns = [
    path ('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('fiction/',views.fiction, name='fiction'),
    path('detail/',views.detail, name="detail"),
    path('signup/', views.signup, name='signup'),
    path('search/',views.search_results,name='search_results')
]