from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('products/<product>/<product_id>', views.suit, name="productcat"),
    path('signup', views.signup, name="signup"), #signup page
]