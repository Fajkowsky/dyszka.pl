from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^user/', 'landingpage.views.user_json'),
)
