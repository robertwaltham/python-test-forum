from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.LandingView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.ForumDetailView.as_view()),
    url(r'^\d+/(?P<pk>\d+)/$', views.ThreadDetailView.as_view()),
    url(r'^login/$', views.LogInView.as_view()),
    url(r'^logout/$', views.LogOutView.as_view()),
    url(r'^signup/$', views.SignUpView.as_view()),
    url(r'^new-forum/$', views.ForumCreationView.as_view(), name='new_forum')

)