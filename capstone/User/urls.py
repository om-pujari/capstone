from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView
from . import views
from Bike.models import Bike
from django.contrib.auth import views as auth_views


app_name = "User"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('wishlist/toggle/<int:bike_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('profile/', views.user_profile, name='profile'),

    path('password_reset/', views.CustomPasswordResetView.as_view(
        success_url='/user/password_reset/done/'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='User/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='User/password_reset_confirm.html',
        success_url='/user/reset/done/'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='User/password_reset_complete.html'),
         name='password_reset_complete'),
]