from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^blog/$', views.BlogListView.as_view(), name="blog"),
    url(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name="post"),
    url(r'^portfolio/$', views.portfolio, name="portfolio"),
]