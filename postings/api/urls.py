from django.urls import path
from .views import BlogPostRudView, BlogPostAPIView
app_name = 'api-postings'

urlpatterns = [
    path('', BlogPostAPIView.as_view()),
    path('<int:pk>/', BlogPostRudView.as_view(), name='post-rud'),
]
