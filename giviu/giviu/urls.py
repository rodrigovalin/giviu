from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'giviu.views.home', name='home'),
    url(r'^giftcard/detail/(?P<gift_id>\d+)$', 'giviu.views.giftcard_detail', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
