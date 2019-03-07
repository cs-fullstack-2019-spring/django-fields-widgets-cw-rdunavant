from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        labels = {

        }
     ABILITY_CHOICES= (
         ('flight'),
         ('speed'),
         ('invisibility'),
         ('telekinetic'),
         ('healing'),
         ('other'),
     )

     QUALITY_CHOICES= (
         ('good'),
         ('kinda good'),
         ('neutral'),
         ('a little evil'),
         ('evil'),
     )
        widgets = {
            "name": forms.NameInput(),
            "cityOrOrigin": forms.cityOrOriginInput(),
            "richOrSuperpower": forms.Select(choices=[("rich", "superpower")]),
            "superPowers": forms.RadioSelect(choices=[("flight", "speed", "invisibility", "telekenetic", "healing", "other")]),
            "you": forms.RadioSelect(choices=[("good", "kinda good", "neutral", "a little evil", "evil")]),
            "examples": forms.examplesInput(),
            "dropDown": forms.SelectMultiple(choices=ABILITY_CHOICES),
            "radio": forms.RadioSelect(choices=QUALITY_CHOICES),
        }