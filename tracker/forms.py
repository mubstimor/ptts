from django import forms
from tracker.models import Contact

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    #sender = forms.EmailField()
    sender = forms.EmailField(
        label=("Your Email Address"),
        max_length=255,
    )
    name = forms.CharField()
    cc_myself = forms.BooleanField(required=False)
    message = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'class': 'span8'},),)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['class'] = 'span7'
        self.fields['sender'].widget.attrs['class'] = 'span7'
        self.fields['name'].widget.attrs['class'] = 'span7'