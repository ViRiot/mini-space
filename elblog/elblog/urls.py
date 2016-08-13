from django.conf.urls import url
from django.contrib import admin
from posts import views
from django.contrib.auth import views as djangoViews 
#from accounts import urls as cuentasUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
    url(r'^blog/$', views.ListView.as_view(), name="lista"),
    url(r'^presentacion/$', views.BaseView.as_view(), name="presentacion"),
   # url(r'^login/$', djangoViews.login, name="login"),
  #  url(r'^accounts/', include(cuentasUrls))

]
