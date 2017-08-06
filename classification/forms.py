from django import forms

class ReviewForm(forms.Form):
    review_choices = (
            (1, 'Positivo'),
            (0, 'Neutro'),
            (-1, 'Negativo')
            )
    review = forms.ChoiceField(choices=review_choices, required=True, label='Opinião do tweet', widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    ironic = forms.BooleanField(required=False, label='É irônico?', widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    tweet = forms.IntegerField(widget=forms.HiddenInput())
    tweet_text = forms.CharField(widget=forms.Textarea(attrs={'disabled': 'disabled', 'class': 'form-control'}))
