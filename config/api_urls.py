from rest_framework.routers import DefaultRouter

from sagittarius.post import views as post_views


router = DefaultRouter()
router.register(r'posts', post_views.PostViewSet, base_name='posts')
urlpatterns = router.urls

