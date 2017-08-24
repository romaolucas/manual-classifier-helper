from django import forms

class ReviewForm(forms.Form):
    review_choices = (
            (1, 'Positivo'),
            (0, 'Neutro'),
            (-1, 'Negativo')
            )
    review = forms.ChoiceField(choices=review_choices, required=True, label='Opinião do tweet', widget=forms.RadioSelect())
    ironic = forms.BooleanField(required=False, label='É irônico?', widget=forms.CheckboxInput(attrs={'class': 'checkbox-inline'}))
    tweet = forms.IntegerField(label='Tweet', widget=forms.HiddenInput())
    tweet_text = forms.CharField(required=False, label='Texto ', widget=forms.Textarea(attrs={'disabled': 'disabled', 
        'class': 'form-control tweet-textarea', 'rows': '3', 'cols': '10'}))


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Arquivo csv (atenção, os elementos devem ser separados por virgula)')
