from rest_framework.routers import DefaultRouter

from .views import CatalogLibrary, CreateAuthor, CreateLibrary, GetBookItem, CreateRack

router = DefaultRouter()
router.register(r'library',CreateLibrary)
router.register(r'Rack',CreateRack)
router.register(r"catalog", CatalogLibrary)
router.register(r'authors', CreateAuthor)
router.register(r'items', GetBookItem)
# router.register(r'rent',RentBook)
urlpatterns = router.urls
