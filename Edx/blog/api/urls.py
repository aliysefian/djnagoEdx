from rest_framework.routers import DefaultRouter

from blog.api.views import BlogPostModelViewSet

router = DefaultRouter()
router.register(r'post', BlogPostModelViewSet, basename='post')
urlpatterns = router.urls
