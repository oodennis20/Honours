from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$',views.logout_request,name="logout"),   
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^all/(?P<pk>\d+)', views.all, name='all'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/', views.upload_project, name='upload'),
    url(r'^review/(?P<pk>\d+)',views.add_review,name='review'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view())

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)