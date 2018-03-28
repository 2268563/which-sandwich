from django.conf.urls import url
from whichsandwich import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^my_account/$', views.my_account, name='my_account'),
        url(r'^my_account/my_sandwiches/$', views.my_sandwiches, name='my_sandwiches'),
        url(r'^my_account/my_favourites/$', views.my_favourites, name='my_favourites'),
        url(r'^create_sandwich/$', views.create_sandwich, name='create_sandwich'),
        url(r'^browse/$', views.browse, name='browse'),
        url(r'^browse_filter/$', views.browse_filter, name='browse_filter'),
        url(r'^modal/$', views.modal, name='modal'),
        url(r'^browse/(?P<sandwich_slug>[\w\-]+)/$', views.show_sandwich, name='show_sandwich'),
        url(r'^browse/(?P<sandwich_slug>[\w\-]+)/comment/$', views.comment, name='comment'),
        url(r'^like/$', views.like_sandwich, name='like_sandwich'),
        url(r'^dislike/$', views.dislike_sandwich, name='dislike_sandwich'),
        url(r'^favourite/$', views.add_to_favourites, name='favourite_sandiwich'),
        ]
