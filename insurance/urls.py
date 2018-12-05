from django.urls import path
from . import views


app_name = 'insurance'
urlpatterns = [
        # employee
    path('employee/add/', views.create_employee,
         name='create-employee'),
    path('employee/delete/<int:pk>/<int:page>/', views.delete_employee,
         name='delete-employee'),
    path('employee/update/<int:pk>/', views.update_employee,
         name='update-employee'),
    path('employees/', views.list_employee, name='list-employee'),
        # family
    path('employee/<int:pk>/', views.detail_employee,
         name='detail-employee'),
    path('employee/<int:pk>/add-family/', views.create_family,
         name='create-family'),
    path('employee/<int:pk>/update-family/<int:pk2>/', views.update_family,
         name='update-family'),
    path('employee/<int:pk>/delete-family/<int:pk2>/', views.delete_family,
         name='delete-family'),
        # relation
    path('list-relation/', views.list_relation, name='list-relation'),
    path('create-relation/', views.create_relation,
         name='create-relation'),
    path('update-relation/<int:pk>/', views.update_relation,
         name='update-relation'),
    path('delete-relation/<int:pk>/', views.delete_relation,
         name='delete-relation'),
]
