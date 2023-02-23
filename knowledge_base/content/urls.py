from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add_article),
    path('gtc', views.gtc),
    path('imprint', views.imprint)
]
