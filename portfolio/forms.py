from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'w3-input w3-border'})
        self.fields['email'].widget.attrs.update({'class': 'w3-input w3-border'})
        self.fields['message'].widget.attrs.update({'class': 'w3-input w3-border'})

    class Meta:
        model = Contact
        fields = '__all__'
