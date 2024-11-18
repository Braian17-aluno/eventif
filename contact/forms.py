from django import forms

class FormularioContato(forms.Form):
  name = forms.CharField(label='Nome')
  telefone = forms.CharField(label='Telefone')
  email= forms.EmailField(label='Email')
  menssagem = forms.CharField(widget=forms.Textarea)