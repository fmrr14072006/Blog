from django.urls import path
from .views import HomepageView, AboutPageView, BlogDetailView, BlogCreateView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name='post_detail'),
    path("post/new", BlogCreateView.as_view(), name="post_new")
]
