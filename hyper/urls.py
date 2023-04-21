from rest_framework.routers import SimpleRouter
from .views import MettoViewSet,iPhoneViewSet


router = SimpleRouter()

router.register('metto', MettoViewSet)
router.register('iphone', iPhoneViewSet)

urlpatterns = [

]