from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'w3-input w3-border'}))
    password = forms.PasswordInput(label='Message', widget=forms.Textarea(
        attrs={'class': 'w3-input w3-border'}))
