from django.conf.urls import url
from whichsandwich import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^my_account/my_sandwiches/$', views.my_sandwiches, name='my_sandwiches'),
    url(r'^my_account/my_favourites/$', views.my_favourites, name='my_favourites'),
    url(r'^create_sandwich/$', views.create_sandwich, name='create_sandwich'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^browse/top/$', views.top, name='top'),
    url(r'^browse/new/$', views.new, name='new'),
    url(r'^browse/controversial/$', views.controversial, name='controversial'),
    url(r'^browse/(?P<sandwich_slug>[\w\-]+)/$', views.show_sandwich, name='show_sandwich'),
	url(r'^browse/(?P<sandwich_slug>[\w\-]+)/comment/$', views.comment, name='comment'),
	url(r'^like/$', views.like_sandwich, name='like_sandwich'),
	url(r'^dislike/$', views.dislike_sandwich, name='dislike_sandwich'),
	url(r'^favourite/$', views.add_to_favourites, name='favourite_sandiwich'),
]
