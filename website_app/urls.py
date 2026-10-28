

from django.urls import path
from website_app import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout_view,name="logout_view"),
    path('record/<int:pk>/',views.record_detail,name="record_detail"),
    path('record/delete/<int:pk>/',views.record_delete,name="record_delete"),
    path('record/update/<int:pk>/',views.record_update,name="record_update"),
    path('record/create/',views.record_create,name="record_create"),
 ]
