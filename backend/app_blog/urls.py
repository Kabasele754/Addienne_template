from django.urls import path
from .views import *

urlpatterns = [
    path('', all_blog, name='all_blog'),
    path('blog_list', BlogListAPIView.as_view(), name="blogs"),
    path('<int:id>', BlogDetailAPIView.as_view(), name="blog"),
]
