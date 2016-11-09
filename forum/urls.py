from django.conf.urls import url
from . import views

app_name = 'forum'


urlpatterns = [

    # /forum/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /forum/read
    url(r'^read/$', views.ReadView.as_view(), name='read'),

    # /forum/profile
    url(r'^profile/$', views.MyView.as_view(), name='profile'),

    # /forum/id
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),

    # /forum/question/add
    url(r'question/add/$', views.QuestionCreate.as_view(), name='question-add'),

    # /forum/question/pk
    url(r'question/(?P<pk>[0-9]+)/$', views.QuestionUpdate.as_view(), name='question-update'),

    # /forum/question/pk/delete
    url(r'question/(?P<pk>[0-9]+)/delete/$', views.QuestionDelete.as_view(), name='question-delete'),

    # /forum/question/pk/ans
    url(r'question/(?P<pk>[0-9]+)/ans/$', views.AnswerCreate.as_view(), name='answer-add'),

    # /forum/answer/update/pk
    url(r'answer/update/(?P<pk>[0-9]+)/$', views.AnswerUpdate.as_view(), name='answer-update'),

    # /forum/answer//delete/pk
    url(r'answer/delete/(?P<pk>[0-9]+)/$', views.AnswerDelete.as_view(), name='answer-delete'),

    # /forum/register
    url(r'^register/$',views.UserFormView.as_view(), name='register'),

    # /forum/logout
    url(r'^forum/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/forum/login'}, name='logout'),

    # /forum/login
    url(r'^login/$', views.login_user, name='login'),

    # /forum/maker
    url(r'^maker/$', views.update_profile, name='adminMaker'),


]
