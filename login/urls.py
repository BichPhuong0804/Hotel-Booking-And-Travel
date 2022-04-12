from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # url(r'', views.index),
    url(r'login/', views.login_user, name='login'),
    url(r'logout/', views.logout_user, name='logout'),
    url(r'register/', views.register, name='register'),
    url(r'profile/', views.edit_profile, name='profile'),
    url(r'contact/', views.contact, name='contact'),
    url(r'change_password/', views.change_password, name='change_password'),
    url(r'change_success/', views.change_success, name="change_success"),
    url(r'history/', views.history, name="history"),
    path('activate/<uidb64>/<token>', views.activate,name = 'activate'),
    path('delete_order/<int:booking_id>', views.deleteOrder, name='delete_order'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]