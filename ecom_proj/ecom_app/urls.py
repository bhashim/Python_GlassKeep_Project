from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('about', views.about),
    path('purchase', views.purchase_confirmation),
    path('purchase/add', views.purchase),
    path('purchase/<int:purchase_id>', views.display_purchase),
    path('purchase/checkout/<int:purchase_id>', views.confirm_display_purchase),
    path('orders', views.orders),
    path('orders/edit/<int:purchase_id>', views.edit_order),
    path('ordersprocess/edit/<int:purchase_id>/process', views.process_order),
    path('orders/<int:purchase_id>/delete', views.delete_order)

]
