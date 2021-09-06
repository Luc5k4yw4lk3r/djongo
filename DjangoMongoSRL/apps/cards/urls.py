from rest_framework import routers, urlpatterns
from .views import CardsViewSet

router = routers.SimpleRouter()
router.register('', CardsViewSet)

urlpatterns = router.urls