from rest_framework.routers import DefaultRouter
from .views import SkillViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet)

urlpatterns = router.urls