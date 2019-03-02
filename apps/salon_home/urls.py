from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^stylists$', views.stylists, name="stylists"),
    url(r'^stylists/kacie$', views.stylistKacie, name="stylistKacie"),
    url(r'^stylists/cooki$', views.stylistCooki, name="stylistCooki"),
    url(r'^stylists/kimberly$', views.stylistKimberly, name="stylistKimberly"),
    url(r'^stylists/heather$', views.stylistHeather, name="stylistHeather"),
    url(r'^stylists/maxine$', views.stylistMaxine, name="stylistMaxine"),
    url(r'^stylists/myHuynh$', views.stylistMyHuynh, name="stylistMyHuynh"),
    url(r'^stylists/phuong$', views.stylistPhuong, name="stylistPhuong"),
    url(r'^stylists/myPhan$', views.stylistMyPhan, name="stylistMyPhan"),
    url(r'^stylists/han$', views.stylistHan, name="stylistHan"),
]
