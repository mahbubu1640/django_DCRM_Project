

from django.urls import path
from website_app import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout_view,name="logout_view"),
 ]
