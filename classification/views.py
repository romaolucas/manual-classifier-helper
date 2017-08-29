import logging
import csv
import codecs
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Tweet, Review
from .forms import ReviewForm, CSVUploadForm

def index(request):
    return render(request, 'classification/index.html', None)

def review(request):
    ReviewFormset = formset_factory(ReviewForm, extra=0)
    logger = logging.getLogger('testlogger')
    if request.method == 'POST':
        review_formset = ReviewFormset(request.POST)
        if review_formset.is_valid():
            logger.info('vou começar a registrar as opinioes')
            for review_form in review_formset:
                tweet_id = review_form.cleaned_data.get('tweet')
                review = review_form.cleaned_data.get('review')
                ironic = review_form.cleaned_data.get('ironic')
                reviewed_tweet = Tweet.objects.get(pk=tweet_id)
                user_review = reviewed_tweet.review_set.create(
                        review=review,
                        ironic=ironic
                )
            logger.info('terminei de colocar as opinioes')
            return redirect('classification:all-reviewed')    
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

def generate_csv(request):
    '''
        TODO: refatorar esse metodo para tirar o if do for, fazer isso antes de deployar pra valer
    '''
    logger = logging.getLogger('testlogger')
    logger.info("gerando csv")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tweets_classificados.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'tweet', 'review'])
    reviewed_tweets = Tweet.objects.filter(review__isnull=False)
    for tweet in reviewed_tweets:
        if not tweet.review_set.all()[0].is_ironic():
            writer.writerow([tweet.tweet_username, tweet.tweet_text, tweet.review_set.all()[0].review])
    logger.info("csv gerado!")
    return response 
