from django.urls import path

from . import views

app_name = 'invites'  # namespace for urls (optional)
urlpatterns = [
    path('all/', views.InviteListView.as_view(), name='invite_list'),
    path('create/?team=<int:pk>', views.InviteCreateView.as_view(), name='invite_user'),
    path('<int:pk>/details/', views.InviteDetailsView.as_view(), name='invite_details'),
    path('<int:pk>/reject/', views.InviteRejectView.as_view(), name='invite_reject'),
    path('<int:pk>/accept/', views.InviteAcceptView.as_view(), name='invite_accept'),
]