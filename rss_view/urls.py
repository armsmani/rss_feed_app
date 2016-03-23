# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('rss_view.views',
                url(r'^$', 'feedreader'),
                url(r'^display', 'feed_render'),
                url(r'^feed_display', 'feed_display')
            )
