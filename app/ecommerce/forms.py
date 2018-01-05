from django import forms

class contactsForm(forms.Form):
    full_name = forms.CharField(widget = forms.TextInput(attrs= {
        'class':'form-control',
        'placeholder':'your full name'
    }))

    email = forms.EmailField(widget = forms.EmailInput(attrs = {
        'class':'form-control',
        'placeholder': 'your email'
    }))

    content = forms.CharField(widget = forms.Textarea(attrs = {
        'class':'form-control',
        'placeholder':'your content'
    }))


class loginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class':'form-control',
        'placeholder':'username'
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class':'form-control',
        'placeholder':'password'
    }))


class registerForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs = {
        'class':'form-control',
        'placeholder':'Your full name'
    }))
    Username = forms.CharField(widget = forms.TextInput(attrs = {
        'class':'form-control',
        'placeholder':'Your username'
    }))
    email = forms.EmailField(widget = forms.EmailInput(attrs = {
        'class':'form-control',
        'placeholder': 'your email'
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class':'form-control',
        'placeholder':'password'
    }))
