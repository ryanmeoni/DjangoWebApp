from django.test import TestCase
from . include views
# Create your tests here.

urlpatterns = [
    path('', views.home, name = "blog-home")
    path('about/', views.about, name = "blog-about")
]
