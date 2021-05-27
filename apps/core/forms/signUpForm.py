from django import forms
from django.contrib.auth import get_user_model

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','user_type']

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'user_type': 'Tipo de Usuario'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'Nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Apellidos'}),
            'user_type': forms.TextInput(attrs={'placeholder':'Tipo de Usuario'})
        }

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = self.cleaned_data['user_type']
        user.save()