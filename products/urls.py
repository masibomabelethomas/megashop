from django.urls import path
from . import views
urlpatterns =[
    path('',views.index),
    path('new', views.new),
    # path('new_arrivals', views.new_arrivals)
]

# add to cart url
# from django.urls import path
# from .views import add_to_cart

# urlpatterns = [
#     # other URL patterns
#     path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
# ]
