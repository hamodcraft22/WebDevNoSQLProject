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
