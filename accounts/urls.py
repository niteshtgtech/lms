# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *
from . import views

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'library', libraryViewSet)

urlpatterns = [
    path("admin",views.base,name="base"),
    path('api', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
    path('', views.index),
    path("user_login/",views.user_login,name="user_login"),
    path("books/",views.books,name="books"),
    path("create",views.create,name="create"),
    path("delete",views.delete,name="delete")
     
]






