from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_view),
    path('unit/', views.unitview),
    path('item/', views.item_view),
    path('test/', views.test),
    path('supplier/', views.supplier_view),
    path('order/', views.order_view),
    path('employee/', views.employee_view),
    
]
    

    

