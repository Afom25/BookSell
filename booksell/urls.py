from django.urls import path

from . import views

urlpatterns = [
    path ('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('fiction/',views.fiction, name='fiction'),
    path('<int:course_id>',views.detail,name="detail"),  
   
    path('register/', views.register, name="register"),
    path('search/',views.search_results,name='search_results')
]