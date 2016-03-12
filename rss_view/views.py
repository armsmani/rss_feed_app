from django.shortcuts import render
from django.http import HttpResponse
from rss_view.models import *

import feedparser
import json

# Create your views here.
def feedreader(request):
    rssDetails = RssDetails.objects.all()
    for rssDetail in rssDetails:
        rssFeed = feedparser.parse(rssDetail.link)

        for feed in rssFeed.entries:
            news = News()
            news.title = feed.title
            news.content = feed.summary
            news.link = feed.link
            news.published_date = feed.published
            news.save()
    return render(request, 'home.html', {'result': "None"})


def feed_render(request):
    newsDetails = News.objects.all()
    data = [{'title': news.title, 'summary': news.content, 'link': news.link}
                for news in newsDetails]
    result = json.dumps(data)
    return HttpResponse(result, content_type="application/json")


def feed_display(request):
    return render(request, 'feed_render.html', {'result': None})