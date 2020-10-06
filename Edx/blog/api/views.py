from rest_framework.viewsets import ModelViewSet

from blog.api.serializer import BlogPostSerializer
from blog.models import BlogPost


class BlogPostModelViewSet(ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

