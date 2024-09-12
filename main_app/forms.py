from django import forms
from .models import Participation

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['volunteer', 'status', 'date_participated']
        widgets = {
            'date_participated': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date'
                }
            ),
        }
