from . import views
from django.urls import path

app_name = "Bikes"

urlpatterns = [
    path('',views.Bike_List.as_view(),name='list'),
    path('<int:pk>/',views.Bike_Detail.as_view(),name = 'detail'),
    path('<int:pk>/book-test-drive/', views.BookTestDriveView.as_view(), name='book_test_drive'),
]