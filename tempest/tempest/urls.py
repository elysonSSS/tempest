
from django.contrib import admin
from django.urls import path
from app.views import logoutFun,home,main,signup_ajax_function,signin_ajax_function,sobre
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
   path('admin/', admin.site.urls),
   path('reg/',signup_ajax_function,name='reg'),
    path('login/',signin_ajax_function,name='login'),
    path('',main,name='main'),
    path('home/',home,name='home'),
     path('logout/',logoutFun,name='logout'),
    #path('substitua', substitua, name='substitua'),
    path('sobre',sobre, name='sobre'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog')
]