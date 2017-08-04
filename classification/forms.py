from django import forms

class ReviewForm(forms.Form):
    review_choices = (
            (1, 'Positivo'),
            (0, 'Neutro'),
            (-1, 'Negativo')
            )
    review = forms.ChoiceField(choices=review_choices, required=True, label='Opinião do tweet')
    ironic = forms.BooleanField(required=False, label='É irônico?')
    tweet = forms.IntegerField(widget=forms.HiddenInput())
    tweet_text = forms.CharField(widget=forms.Textarea(attrs={'disabled': 'disabled'}))
