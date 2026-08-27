from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Full Name *',
            'id': 'contact-name'
        })
    )
    phone = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Phone Number (e.g. 0400 000 4T1) *',
            'id': 'contact-phone'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email Address *',
            'id': 'contact-email'
        })
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-input form-textarea',
            'rows': 5,
            'placeholder': 'Tell us about your vehicle, tyre needs or location/yard service details... *',
            'id': 'contact-message'
        })
    )
