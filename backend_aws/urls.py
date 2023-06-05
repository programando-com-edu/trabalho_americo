from django.urls import path
from api_projeto.views import  UserListCreateAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-retrieve-update'),
]