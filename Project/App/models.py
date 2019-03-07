from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=200, default=0)
    cityOrOrigin = models.CharField(max_length=500, default=0)
    booleanItem = models.BooleanField()
    radio = models.ChoiceField("Flight", "Speed", "Invisibility", "Telekenetic", "Healing", "Other")
    you = models.ChoiceField("Good", "kinda good", "neutral", "a little evil", "evil")
    examples = models.CharField()





richOrSuperpower = models.ChoiceField("rich", "superpower")
Superpowers = models.ChoiceField("Flight", "Speed", "Invisibility", "Telekenetic", "Healing", "Other")
you = models.ChoiceField("Good", "kinda good", "neutral", "a little evil", "evil")