from django.conf.urls import patterns, url
from django.contrib import admin
from qa.views import test, question_list, question_detail, popular
from qa.views import question_ask, question_answer


urlpatterns = patterns('',
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^new/', test, name='new'),
    url(r'^admin/', admin.site.urls),
)
