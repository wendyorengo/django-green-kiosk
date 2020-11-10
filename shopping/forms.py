from django import forms
from .models import Product


class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 26)]
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int)
    update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
            

        