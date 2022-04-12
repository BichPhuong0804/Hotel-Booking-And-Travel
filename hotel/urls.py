from django.urls import path
from hotel import views

urlpatterns = [
    path(r'', views.hotel, name="hotel"),
    path(r'detail/<int:hotel_id>/', views.hotel_detail, name="hotel_detail"),
    path(r'booking/<int:hotel_id>/', views.booking, name="booking"),
    path(r'booking_success/', views.success_booking, name="booking_success"),
    path(r'booking/detail/<int:booking_id>', views.booking_detail, name="booking_detail"),
    path("favorite/add/<int:hotel_id>", views.favorite, name='favorite'),
    path("favorite/", views.wishlist, name='user_favorite'),
]
