# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loren.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index'),
    url(
        r'^blog/post/(?P<slug>[^\.]+)', 
        'blog.views.view_post', 
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+)', 
        'blog.views.view_category', 
        name='view_blog_category'),
)
