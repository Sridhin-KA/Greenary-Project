from django.urls import path
from . import views




urlpatterns = [
    path('', views.cart_details, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('place-order', views.PlaceOrder, name='place_order'),
    path('payment/<int:order_id>', views.payments, name='payments'),
    
]

