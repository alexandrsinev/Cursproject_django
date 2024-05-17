from django.urls import path

from user_client.apps import UserClientConfig
from user_client.views import Main, FeedBackView, CreateUserView, UpdateUser, DeleteUser, UserProfile, ClientsListView, \
    CreateClientView

app_name = UserClientConfig.name

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('feedback/', FeedBackView.as_view(), name='feedback'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('edit/<int:pk>', UpdateUser.as_view(), name='update'),
    path('delete/<int:pk>', DeleteUser.as_view(), name='delete'),
    path('detail/<int:pk>', UserProfile.as_view(), name='user_profile'),
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('create1/', CreateClientView.as_view(), name='create_client'),
]
