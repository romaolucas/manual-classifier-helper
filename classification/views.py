from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Tweet, Review
from .forms import ReviewForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'classification/index.html', None)

def review(request):
    ReviewFormset = formset_factory(ReviewForm, extra=0)
    if request.method == 'POST':
        review_formset = ReviewFormset(request.POST)
        logger.info('opa')
        if review_formset.is_valid():
            logger.info('ta tudo certo aqui')
            for review_form in review_formset:
                tweet_id = review_form.cleaned_data.get('tweet')
                review = review_form.cleaned_data.get('review')
                ironic = review_form.cleaned_data.get('ironic')
                reviewed_tweet = Tweet.objects.get(pk=tweet_id)
                user_review = reviewed_tweet.review_set.create(
                        review=review,
                        ironic=ironic
                )
            return redirect('show_reviewed')    
        else:
            context = {'review_formset': review_formset}
            return render(request, 'classification/review.html', context)
    else:
        tweets_amount = int(request.GET['tweets_amount'])
        tweets_to_review = Tweet.objects.filter(review__isnull=True)[:tweets_amount]
        initial_values = [{'tweet': tweet.pk, 'tweet_text': tweet.tweet_text} for tweet in tweets_to_review]
        review_formset = ReviewFormset(initial=initial_values)
        context = {'review_formset': review_formset}
        return render(request, 'classification/review.html', context)

def all_reviewed(request):
    reviewed_tweets = Tweet.objects.filter(review__isnull=False)
    context = {'reviewed_tweets' : reviewed_tweets}
    return render(request, 'classification/show_reviewed.html', context)
