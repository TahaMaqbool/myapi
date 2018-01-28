from django.conf.urls import url
from heroes import views

urlpatterns = [
    url(r'^heroes/$', views.heroes_list),
    url(r'^heroes/(?P<pk>[0-9]+)/$', views.hero_detail),
]
