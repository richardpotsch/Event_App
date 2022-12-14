"""EventApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import base.views
import user.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base.views.ListOfEvents.as_view(), name='events'),
    path('one_event/<pk>', base.views.event_detail, name='one_event'),
    path('event_update/<pk>', base.views.EventUpdateView.as_view(), name='event_update'),
    path('event_delete/<pk>', base.views.EventDeleteView.as_view(), name='event_delete'),
    path('search/', base.views.event_search, name='search'),
    path('response/<pk>', base.views.make_event_response, name='response'),
    path('event_form/', base.views.EventCreateView.as_view(), name='event_form'),
    path('signup/', user.views.SignUpView.as_view(), name='signup'),
    path('login/', user.views.LoginView.as_view(), name='login'),
    path('logout/', user.views.LogoutView.as_view(), name='logout'),
]
