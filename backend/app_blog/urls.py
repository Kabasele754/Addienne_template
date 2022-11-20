from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListAPIView.as_view(), name="blogs"),
    path('<int:id>', BlogDetailAPIView.as_view(), name="blog"),
]
