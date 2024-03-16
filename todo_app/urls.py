from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_todo,name='home'),
    path('add/',views.add_todo,name='add'),
    path('update/<int:id>/',views.update_todo,name='update'),
    path('delete/<int:id>/',views.delete_todo,name='delete'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]
