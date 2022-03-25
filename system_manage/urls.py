from rest_framework.routers import DefaultRouter

from .views import CatalogLibrary, CreateAuthor, GetBookItem, RentBook

router = DefaultRouter()
router.register(r"catalog", CatalogLibrary)
router.register(r'authors', CreateAuthor)
router.register(r'items', GetBookItem)
router.register(r'rentbook', RentBook)
urlpatterns = router.urls
