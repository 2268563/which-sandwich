from django.conf.urls import url
from whichsandwich import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
'''
    url(r'^about/$', views.about, name='about'),
    
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),

    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^my_account/my_sandwiches/$', views.my_sandwiches, name='my_sandwiches'),
    url(r'^my_account/my_favourites/$', views.my_favourites, name='my_favourites'),

    url(r'^create_sandwich/$', views.create_sandwich, name='create_sandwich'),

    url(r'^browse/$', views.browse, name='browse'),
    url(r'^browse/top/$', views.top, name='top'),
    url(r'^browse/new/$', views.new, name='new'),
    url(r'^browse/controversial/$', views.controversial, name='controversial'),
    url(r'^browse/sandwich_name/$', views.sandwich_name, name='sandwich_name'),
]
'''



#May need to add a sign_out option (as a view)
#url(r'^sign_out/$', views.user_sign_out, name='sign_out'),
