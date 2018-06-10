"""WorldCup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from WCScores.views import FormsView, MatchFormView, IndexView, ScoresView, LoginView, RegisterView, AddScoreView, \
    UserScoresView, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addcountry$', FormsView.as_view()),
    url(r'^addmatch/$', MatchFormView.as_view()),
    url(r'^$', IndexView.as_view()),
    url(r'^scores/$', ScoresView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^addscore/(?P<id>(\d+))/$', AddScoreView.as_view()),
    url(r'^userscores/(?P<id>(\d+))/$', UserScoresView.as_view()),
    url(r'^logout/$', logout_view),


]
