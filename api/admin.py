from django.contrib import admin
from .models import *

admin.site.register((Food, Hydration, Sleep, SleepRange, Mood, MoodChoice, Digestion, DigestionChoice, Smoking))
