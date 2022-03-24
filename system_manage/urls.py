from rest_framework.routers import DefaultRouter

from .views import CatalogLibrary

router = DefaultRouter()
router.register("catalog", CatalogLibrary)
urlpatterns = router.urls
