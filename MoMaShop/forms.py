from django import forms

CATEGORY_CHOICES = (
    ('si', 'Still Image'),
    ('ai', 'Animated Image'),
    ('cv', 'Customized Video')
)

class addItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()
    image = forms.FileField()

class addCommentForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()

class addToOrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
