from django.conf.urls import url
from .views import CreateUserView
from .views import login
from rest_framework.authtoken import views
from.views import *

urlpatterns = [
    url(r'^register/', CreateUserView.as_view(), name='account-create'),
    url(r'^login/',login,name='login'),
    url(r'^api-token-auth/', views.obtain_auth_token,name='token'),
    url(r'^profiledetails/',profiledetails.as_view(), name='profiledetails'),
    url(r'^posts/', postview.as_view(), name='profiledetails'),
    url(r'^followfollowingview/', followfollowingview.as_view(), name='followfollowing'),
    url(r'^profiledetailsupdate/', profiledetailsupdate.as_view(), name='profilepost_details'),
    url(r'^exp/', exp.as_view(), name='exp'),
    url(r'^bac/', user_bac_view.as_view(), name='sasa'),



]