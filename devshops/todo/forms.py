from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter some supplies...', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))

class TodoForm1(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Enter in big things for the office...', 'aria-label' : 'Todo1', 'aria-describedby' : 'add-btn1'}))
