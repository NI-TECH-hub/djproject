
from django import forms
from .models import TODO

class DateInput(forms.DateInput):
    input_type = 'date'
    


class TodoForm(forms.ModelForm):
    title = forms.CharField(label_suffix='',widget = forms.TextInput(attrs={'class':'form-control'}))
    deadline = forms.DateField(label_suffix='',widget = DateInput())
    class Meta:
        
        model = TODO
        fields = ['title','deadline'] 