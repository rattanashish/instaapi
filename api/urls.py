from django.conf.urls import url
from .views import CreateUserView
from .views import login
from rest_framework.authtoken import views
from.views import listusers,userposts

urlpatterns = [
    url(r'^$', CreateUserView.as_view(), name='account-create'),
    url(r'^login/',login,name='login'),
    url(r'^api-token-auth/', views.obtain_auth_token,name='token'),
    url(r'^users/', listusers.as_view(),name='list '),
    url(r'^posts/', userposts.as_view(), name='posts '),


]