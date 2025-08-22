from django.urls import path
from . import  views

urlpatterns = [
    path('',views.exprnse_list,name='expense_list'),
    path('create/',views.expense_create,name='expense_create'),
    path('<int:pk>/edit/',views.expense_update,name='expense_update'),
    path('<int:pk>/delete/',views.expense_delete,name='expense_delete')

]