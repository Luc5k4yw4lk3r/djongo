from rest_framework import routers, urlpatterns
from .views import RightOwnersViewSet

router = routers.SimpleRouter()
router.register('', RightOwnersViewSet)

urlpatterns = router.urls
