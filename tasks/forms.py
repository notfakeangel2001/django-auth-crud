from .models import Task
from django import forms

#Creando formulario tomand como base el modelo creado previamente
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = { 
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a tittle'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }