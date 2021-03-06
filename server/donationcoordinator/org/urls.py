"""org URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import OrgDetail, OrgCreateOrUpdate, OrgCreate, searchHomeList, OrgItemsUpdate

app_name = 'org'
urlpatterns = [
    # view own org
    path(r'my-org/',
         views.my_org,
         name='index'
         ),

    # create new org
    path(r'new/',
         login_required(
             OrgCreate.as_view()
         ),
         name='new_org'
         ),

    # edit own org
    path(r'orgs/<int:pk>/edit',
         login_required(
             OrgCreateOrUpdate.as_view()
         ),
         name='org_edit',
         ),

    # list of orgs
    path(r'orgs/', views.org_list, name='org_list'),

    # view other org
    path(r'orgs/<int:pk>/',
         OrgDetail.as_view(),
         name='org_detail',
         ),

    path(r'users/',
         login_required(
             searchHomeList
         ),
         name='donator_list',
         ),

    # view or edit Org's items
    path(r'items/',
         login_required(
             OrgItemsUpdate.as_view(),
         ),
         name='org_items'
         ),

    # update Org's items
    path(r'items/update/',
         login_required(
             OrgItemsUpdate.as_view(),
         ),
         name='org_items_update',
         ),

]
