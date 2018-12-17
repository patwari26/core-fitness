from django.urls import path
from django.conf.urls import url,include
from . import views
from .feed import LatestEntriesFeed
"""
urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/category/',views.category,name='category'),
    path('home/tips/',views.tips,name='tips'),
    path('home/contact/',views.contact,name='contact'),
    path('home/about/',views.about,name='about'),

]
"""

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/category/',views.category,name='category'),
    path('home/tips/',views.tips,name='tips'),
    path('home/contact/',views.contact,name='contact'),
    path('home/about/',views.about,name='about'),
    path('home/input/', views.input, name='input'),
    path('',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('feed/', LatestEntriesFeed()),
    path('feedlink/',views.feedlink,name='feedlink'),
    path('dummy/',views.dummy,name='dummy')
]
