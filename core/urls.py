from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CatalogLibrary2

router = DefaultRouter()
router.register(r"", UserViewSet)
router.register(r'catalog/', CatalogLibrary2)
urlpatterns = router.urls
