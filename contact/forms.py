from django import forms

class FormularioContato(forms.Form):
  nome = forms.CharField(label='Nome')
  telefone = forms.CharField(label='Telefone', required=False)
  email= forms.EmailField(label='Email')
  mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)