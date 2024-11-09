from django.urls import path
from .views import UserView

urlpatterns = [
    path('user_profile/', UserView.as_view(), name='post-and-get-user'),
]
