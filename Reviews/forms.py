from django import forms

RATING_OPTIONS = (
("⭐","⭐"),
("⭐⭐","⭐⭐"),
("⭐⭐⭐","⭐⭐⭐"),
("⭐⭐⭐⭐","⭐⭐⭐⭐"),
("⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"))

class reviewForm(forms.Form):
    rating = forms.ChoiceField(choices=RATING_OPTIONS,) ## add limit
    description = forms.CharField(widget=forms.Textarea())
