from django import forms


class TodoForm(forms.Form):
    aim1 = forms.CharField(label='Aim1', max_length=18)
    aim2 = forms.CharField(label='Aim2', max_length=18)
    aim3 = forms.CharField(label='Aim3', max_length=18)
    aim4 = forms.CharField(label='Aim4', max_length=18)
    aim5 = forms.CharField(label='Aim5', max_length=18)
