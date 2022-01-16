from django import forms
from .models import Lead, Agent, UserProfile


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    agent = forms.ModelChoiceField(queryset=Agent.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    organization = forms.ModelChoiceField(queryset=UserProfile.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
