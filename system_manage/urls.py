from rest_framework.routers import DefaultRouter

from .views import CatalogLibrary, CreateAuthor, GetBookItem

router = DefaultRouter()
router.register(r"catalog", CatalogLibrary)
router.register(r'authors', CreateAuthor)
router.register(r'items', GetBookItem)
urlpatterns = router.urls
