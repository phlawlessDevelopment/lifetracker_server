from rest_framework import serializers
from .models import Food, Hydration, Sleep, SleepRange, Mood, MoodChoice, Digestion, DigestionChoice, Smoking

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class HydrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydration
        fields = '__all__'

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = '__all__'


class SleepRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepRange
        fields = '__all__'


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'


class MoodChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodChoice
        fields = '__all__'


class DigestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digestion
        fields = '__all__'


class DigestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigestionChoice
        fields = '__all__'


class SmokingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smoking
        fields = '__all__'
