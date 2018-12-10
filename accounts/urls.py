from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('update_my_profile/', views.update_my_profile, name='update_my_profile'),
    path('change_my_password/', views.change_password, name='change_my_password'),
    path('register/', views.register, name='register'),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('admin_change_password/<int:pk>/', views.admin_change_password, name='admin_change_password'),
    path('users/', views.list_user, name='list_user'),

    ]
