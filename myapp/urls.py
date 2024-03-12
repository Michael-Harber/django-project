from django.urls import path
from . import views

urlpatterns = [
  path("",views.home, name="home"),
  path("about/",views.about, name="about"),
  path('function/', views.function_view, name='function_view'),
  path('contact/', views.contact, name='contact'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('gallery/', views.gallery.as_view(), name='gallery'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('movies/', views.movies.as_view(), name='movies'),
  path('books/', views.books.as_view(), name='books'),
]

