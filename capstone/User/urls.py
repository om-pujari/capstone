from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView
from . import views
from Bike.models import Bike

app_name = "User"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('wishlist/toggle/<int:bike_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('profile/', views.user_profile, name='profile'),
]