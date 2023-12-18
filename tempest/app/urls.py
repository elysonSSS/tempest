from django.contrib import admin
from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('home',views.home, name='home'),
    #path('substitua', views.substitua, name='substitua'),
    path('sobre',views.sobre, name='sobre'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('sucesso', views.sucesso, name='sucesso'),
]