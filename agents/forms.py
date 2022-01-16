from leads.models import Agent, UserProfile, User
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AgentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # user = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=User.objects.all())
    # organization = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
    #                                       queryset=UserProfile.objects.all())
