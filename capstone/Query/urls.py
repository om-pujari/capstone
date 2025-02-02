from django.urls import path
from .views import Query_Form
app_name = "contact"

urlpatterns = [
    path('',Query_Form.as_view(),name="query"),
]