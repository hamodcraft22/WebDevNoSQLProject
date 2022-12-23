from django import forms


PAYMENT_CHOICES = (
    ('cc', 'Credit Card'),
    ('dc', 'Debit Card')
)

class addItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()
    image = forms.FileField()

class addCommentForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())

class addToOrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', "placeholder":"quantity"}))


class checkoutForm(forms.Form):
    paymentType = forms.ChoiceField(choices=PAYMENT_CHOICES)
    cardNum = forms.IntegerField()
    cardExp = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    comments = forms.CharField(widget=forms.Textarea())
