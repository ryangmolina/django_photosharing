from django.urls import path

from . import views

app_name = 'photosharing'  # namespace for urls (optional)
urlpatterns = [
    path('', views.PhotoListView.as_view(), name='home'),
    path('team/all', views.TeamListView.as_view(), name='team_list'),
    path('team/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team/<int:pk>/details', views.TeamDetailView.as_view(), name='team_details'),
    path('team/<int:pk>/upload/', views.PhotoUploadView.as_view(), name='team_photo_upload'),
    path('photo/<int:pk>/all/', views.TeamPhotoListView.as_view(), name='team_photo_list'),
    path('photo/<int:pk>/details/', views.PhotoDetailView.as_view(), name='photo_details'),
]
