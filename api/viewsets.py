from rest_framework import viewsets
from .serializers import *
from .models import *

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

class HydrationViewSet(viewsets.ModelViewSet):
    serializer_class = HydrationSerializer
    queryset = Hydration.objects.all()

class SleepViewSet(viewsets.ModelViewSet):
    serializer_class = SleepSerializer
    queryset = Sleep.objects.all()

class SleepRangeViewSet(viewsets.ModelViewSet):
    serializer_class = SleepRangeSerializer
    queryset = SleepRange.objects.all()

class MoodViewSet(viewsets.ModelViewSet):
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()

class MoodChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = MoodChoiceSerializer
    queryset = MoodChoice.objects.all()

class DigestionViewSet(viewsets.ModelViewSet):
    serializer_class = DigestionSerializer
    queryset = Digestion.objects.all()

class DigestionChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = DigestionChoiceSerializer
    queryset = DigestionChoice.objects.all()

class SmokingViewSet(viewsets.ModelViewSet):
    serializer_class = SmokingSerializer
    queryset = Smoking.objects.all()



