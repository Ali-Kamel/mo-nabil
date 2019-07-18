from django import forms


class Email(forms.Form):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        }
    ))

    email = forms.EmailField(max_length=50,  required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    phone_num = forms.IntegerField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number'
        }
    ))
    message = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Message'
        }
    ))
