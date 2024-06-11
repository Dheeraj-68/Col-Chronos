from django.urls import path
from . import views
from .views import table_detail

urlpatterns = [
    
    path('',views.home,name='home'),
    path('homepage',views.homepage,name='homepage'),
    path('viewinfo',views.viewinfo,name='viewinfo'),
    path('createtable',views.createtable,name='createtable'),
    path('Login' , views.Login , name="Login"),
    path('Logout' , views.Logout , name="Logout"),
    path('viewinfo/<str:table_name>', views.table_detail, name='table_detail'),
    path('prebuildinfo', views.prebuildinfo, name='prebuildinfo'),
    path('tablebuilder', views.tablebuilder, name='tablebuilder'),
]