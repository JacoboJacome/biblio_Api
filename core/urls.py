from rest_framework.routers import DefaultRouter

# from core.serializers import RentBookSerializer

from .views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet)
# router.register(r'rent/', RentBook)
urlpatterns = router.urls
