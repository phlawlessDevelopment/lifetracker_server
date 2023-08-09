
from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()

router.register('food', FoodViewSet, basename='food')
router.register('hydration', HydrationViewSet, basename='hydration')
router.register('sleep', SleepViewSet, basename='sleep')
router.register('sleep_range', SleepRangeViewSet, basename='sleep_range')
router.register('mood', MoodViewSet, basename='mood')
router.register('mood_choice', MoodChoiceViewSet, basename='mood_choice')
router.register('digestion', DigestionViewSet, basename='digestion')
router.register('digestion_choice', DigestionChoiceViewSet, basename='digestion_choice')
router.register('smoking', SmokingViewSet, basename='smoking')

urlpatterns = router.urls
