from rest_framework.routers import SimpleRouter
from .views import BlogViewSet


router = SimpleRouter()

router.register('blog', BlogViewSet)

urlpatterns = [

]