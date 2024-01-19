from django.urls import path
from ShopEzy_App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("customer_signup", views.customer_signup, name="customer_signup"),
    path("customer_signin", views.customer_signin, name="customer_signin"),
    path("customer_profile/<int:customer_id>", views.customer_profile, name="customer_profile"),
    path("product_view/<int:customer_id>", views.product_view, name="product_view"),
    path("product_detail/<str:category_name>/<int:customer_id>", views.product_detail, name="product_detail"),
    path("order_confirmation", views.order_confirmation, name="order_confirmation"),
    path("shopping_history", views.shopping_history, name="shopping_history"),
    path("customer_signout/<int:customer_id>", views.customer_signout, name="customer_signout"),
    path("cart/<int:customer_id>/<str:category_name>", views.cart, name="cart"),
]