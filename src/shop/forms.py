from django import forms
from shop.models import ShippingAddress


class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'customer',
            'id': 'customer',
            'type': 'text',
            'placeholder': 'example',
        })
        self.fields['order'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'order',
            'id': 'order',
            'type': 'text',
            'placeholder': '',
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'address',
            'id': 'address',
            'type': 'text',
            'placeholder': 'Main Street 23A',
        })
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'city',
            'id': 'city',
            'type': 'text',
            'placeholder': 'Kiev',
        })
        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'state',
            'id': 'state',
            'type': 'city',
            'placeholder': 'Ukraine',
        })
        self.fields['zipcode'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'zipcode',
            'id': 'zipcode',
            'type': 'text',
            'placeholder': 'New York',
        })

    class Meta:
        model = ShippingAddress
        fields = ('customer', 'order', 'address', 'city', 'state', 'zipcode')
