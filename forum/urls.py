from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home-page"),
    path("highlighted/", views.MostRatedCarsView.as_view(), name="highlighted"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name='follow-user'),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name='unfollow-user'),
    path("notification/read/<int:notification_id>/", MarkNotificationAsReadView.as_view(),
         name='mark-notification-as-read'),
    path("notification/read/all/", MarkAllNotificationsAsReadView.as_view(), name='mark-all-notifications-as-read'),
    path("profile/<slug:username>/", views.ProfileView.as_view(), name="profile"),
    path("posts/<slug:pk>/", views.PostDetailView.as_view(), name="post-detail"),

]
