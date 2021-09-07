from rest_framework import routers, urlpatterns
from .views import MusicsViewSet, TitlesViewSet

router = routers.SimpleRouter()
router.register('', MusicsViewSet)
# router.register('title', TitlesViewSet)

urlpatterns = router.urls