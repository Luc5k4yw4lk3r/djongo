from rest_framework import routers
from .views import MusicsViewSet

router = routers.SimpleRouter()
router.register('', MusicsViewSet)

urlpatterns = router.urls