from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dualviewproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'dualview.views.home_page', name='home'),
     url(r'^dual_view/', 'dualview.views.dual_view', name='dual_view'),
     url(r'^main_controls/', 'dualview.views.main_controls', name='main_controls'),
     url(r'^img_controls/', 'dualview.views.img_controls', name='img_controls'),
     
)
