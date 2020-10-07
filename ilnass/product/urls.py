from django.urls import path
from .views      import Allproducts, RecommendView, DetailView, Basicinformation
urlpatterns = [
    path('',Allproducts.as_view()),
    path('/recommend',RecommendView.as_view()),
    path('/detail',DetailView.as_view()),
    path('/creator',Basicinformation.as_view()),
]