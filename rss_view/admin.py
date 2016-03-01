from django.contrib import admin

from rss_view.models import News, RssDetails


admin.site.register(News)
admin.site.register(RssDetails)

