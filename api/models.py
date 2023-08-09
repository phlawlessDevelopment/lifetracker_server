from django.db import models

class LifetrackModel(models.Model):
    notes = models.CharField(max_length=256, null=True, blank=True)
    date_time = models.DateTimeField()


class Food(LifetrackModel):
    meal = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.meal} - {self.date_time}'

class Hydration(LifetrackModel):
    drink = models.CharField(max_length=256)
    mesurement = models.CharField(max_length=256)
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.drink} - {self.mesurement} - {self.amount} - {self.date_time}'

class Sleep(LifetrackModel):
    
    def __str__(self):
        return f'{self.date_time}'


class SleepRange(models.Model):
    from_time = models.TimeField()
    to_time = models.TimeField()
    sleep = models.ForeignKey(Sleep, on_delete=models.CASCADE, related_name='times')

    def __str__(self):
        return f'{self.from_time} - {self.to_time}'

class Mood(LifetrackModel):

    def __str__(self):
        return f'{self.date_time}'

class MoodChoice(models.Model):
    text = models.CharField(max_length=64)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return f'{self.text}'

class Digestion(LifetrackModel):
    
    def __str__(self):
        return f'{self.date_time}'

class DigestionChoice(models.Model):
    text = models.CharField(max_length=64)
    digestion = models.ForeignKey(Digestion, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return f'{self.text}'
    
class Smoking(LifetrackModel):
    count = models.PositiveSmallIntegerField()
    weight = models.FloatField()
    def __str__(self):
        return f'{self.date_time}'

