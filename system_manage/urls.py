from rest_framework.routers import DefaultRouter

from .views import CatalogLibrary, CreateAuthor,RentBook ,CreateLibrary, CreateRack,CreateBookItem, GiveOutBook 

router = DefaultRouter()
router.register(r'library',CreateLibrary)
router.register(r'Rack',CreateRack)
router.register(r'authors', CreateAuthor)
router.register(r'catalog', CatalogLibrary)
router.register(r'bookitems', CreateBookItem)
router.register(r'rent', RentBook)
router.register(r'give_out', GiveOutBook)

urlpatterns = router.urls

