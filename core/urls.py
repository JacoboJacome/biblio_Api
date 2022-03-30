from rest_framework.routers import DefaultRouter

from .views import UserViewSet, BooksUser

router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r"rent/books", BooksUser)
urlpatterns = router.urls
