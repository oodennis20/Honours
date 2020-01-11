from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^$',views.home,name='home')
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$',views.logout_request,name="logout"),   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)