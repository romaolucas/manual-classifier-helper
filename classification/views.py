from django.shortcuts import render
from django.forms import formset_factory
from .models import Tweet, Review
from .forms import ReviewForm

def index(request):
    return render(request, 'classification/index.html', None)

def review(request):
    ReviewFormset = formset_factory(ReviewForm, extra=0)
    if request.method == 'POST':
        review_formset = ReviewFormset(request.POST)
        for review_form in review_formset:
            tweet_id = review_form.cleaned_data.get('tweet')
            review = review_form.cleaned_data.get('review')
            ironic = review_form.cleaned_data.get('ironic')
            reviewed_tweet = Tweet.objects.get(pk=tweet_id)
            user_review = Review.objects.get_or_create(tweet=reviewed_tweet)
            user_review.review = review
            user_review.ironic = ironic
            user_review.save()
    else:
        tweets_amount = int(request.GET['tweets_amount'])
        tweets_to_review = Tweet.objects.filter(review__isnull=True)[:tweets_amount]
        initial_values = [{'tweet': tweet.pk, 'tweet_text': tweet.tweet_text} for tweet in tweets_to_review]
        review_formset = ReviewFormset(initial=initial_values)
        context = {'review_formset': review_formset}
        return render(request, 'classification/review.html', context)
