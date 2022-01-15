from leads.models import Agent, UserProfile, User
from django import forms


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['user']

    user = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=User.objects.all())
    # organization = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
    #                                       queryset=UserProfile.objects.all())
