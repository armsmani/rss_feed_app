# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('rss_view.views',
                url(r'^reader', 'feed_reader'),
                url(r'^display', 'feed_render')
            )
