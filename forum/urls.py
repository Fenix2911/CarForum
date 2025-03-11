from django.urls import path, include

from . import views
from .views import FollowUserView, UnfollowUserView, MarkNotificationAsReadView, MarkAllNotificationsAsReadView

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home-page"),
    path("highlighted/", views.MostRatedCarsView.as_view(), name="highlighted"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name='follow_user'),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name='unfollow_user'),
    path("notification/read/<int:notification_id>/", MarkNotificationAsReadView.as_view(),
         name='mark_notification_as_read'),
    path("notification/read/all/", MarkAllNotificationsAsReadView.as_view(), name='mark_all_notifications_as_read'),
    path("profile/<slug:username>/", views.ProfileView.as_view(), name="profile"),

]
