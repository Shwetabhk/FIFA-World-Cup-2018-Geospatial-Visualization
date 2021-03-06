"""FIFA2018 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from Home.views import home, tv_channels, stadiums, teams
from User.views import register_page, login_page, logout_page
from Matches.views import matches,comments


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^stadiums/$', stadiums),
    url(r'^teams/$', teams),
    url(r'^channels/$', tv_channels),
    url(r'^matches/$', matches),
    url(r'^comments/$', comments),
    url(r'^register/$', register_page),
    url(r'^login/$', login_page),
    url(r'^logout/$', logout_page)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
