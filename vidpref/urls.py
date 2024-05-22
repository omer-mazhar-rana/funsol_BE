from django.urls import path

from .views import (
    UserLoginView,
    UserPreferenceView,
    VideoStatisticDownloadsListView,
    VideoStatisticSharesListView,
    VideoStatisticView,
    VideoStatisticViewsListView,
    VideoView,
)

urlpatterns = [
    # User related URLs *****
    path("login/", UserLoginView.as_view(), name="login-user"),  # user login
    path(
        "preferences/", UserPreferenceView.as_view(), name="add-user-preferences"
    ),  # user to use this to add preferences
    path(
        "preferences/retrieve/",
        UserPreferenceView.as_view(),
        name="retrieve-user-preferences",
    ),  #  user to retrieve all it's preferences
    path(
        "preference/update/<int:record_id>/",
        UserPreferenceView.as_view(),
        name="update-user-preferences",
    ),  #  user to update preferences
    path(
        "preferences/retrieve/<str:preference>/",
        UserPreferenceView.as_view(),
        name="retrieve-particular-user-preference",
    ),  # user to retrieve specific preference
    # Video related URLs *****
    path("videos/", VideoView.as_view(), name="add-video"),  # add a new video
    path(
        "videos/retrieve/",
        VideoView.as_view(),
        name="retrieve-videos-for-user",
    ),  # retrieve videos for user based on his preferences
    # Video statistics related URLs *****
    path(
        "video-statistics/",
        VideoStatisticView.as_view(),
        name="add-video-statistics",
    ),  # add video stats
    path(
        "video-statistics/<int:video_id>/",
        VideoStatisticView.as_view(),
        name="video-statistics-detail",
    ),  # video statistics detail
    path(
        "video-statistics/views/<int:video_id>/",
        VideoStatisticViewsListView.as_view(),
        name="video-views-list",
    ),  # video views stats
    path(
        "video-statistics/shares/<int:video_id>/",
        VideoStatisticSharesListView.as_view(),
        name="video-shares-list",
    ),  # video shares stats
    path(
        "video-statistics/downloads/<int:video_id>/",
        VideoStatisticDownloadsListView.as_view(),
        name="video-downloads-list",
    ),  # video downloads stats
]
