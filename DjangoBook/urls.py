from django.conf.urls import patterns, include, url
from django.contrib import admin
from DjangoBook.views import time, future, home_method, display_meta
from books_app.views import search_book, book_res

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^time/$', time, name='time'), #can do just with import
    url(r'^time/plus/(\d+)/$', future),
    url(r'^time/plus/$', future),
    url(r'^home/$', home_method),
    url(r'^books/$', search_book),
    url(r'^book/found/$', book_res),
    url(r'^meta/$', display_meta),
    url(r'^admin/', include(admin.site.urls)),
)
