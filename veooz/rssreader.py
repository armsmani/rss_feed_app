# -*- coding: utf-8 -*-
from rss_view.models import RssDetails, News
import feedparser


class RssReader:

    def __init__(self):
        pass

    def parser(self):
        rssDetails = RssDetails.objects.all()
        for rssDetail in rssDetails:
            rssFeed = feedparser.parse(rssDetail.link)

            for feed in rssFeed:
                news = News()
                news.title = feed.title
                news.content = feed.summary
                news.link = feed.link
                news.published_date = feed.published
                news.save()


if __name__ == '__main__':
    rssReader = RssReader()
    rssReader.parser()