from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Preferences, Video, VideoStatistics
from .serializers import (
    PreferencesSerializer,
    VideoSerializer,
    VideoStatisticSerializer,
)


class UserLoginView(TokenObtainPairView):
    """
    View to log in a user and generate JWT tokens.

    POST request with user login credentials(username and password).
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Log in a user and generate JWT tokens.
        """
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data.get("refresh", None)
        access_token = response.data.get("access", None)
        return Response(
            {
                "refresh": refresh_token,
                "access": access_token,
            },
            status=status.HTTP_200_OK,
        )


class UserPreferenceView(APIView):
    """
    View to manage user preferences.

    POST request to set user preferences, GET request to retrieve user preferences,
    and PUT request to update user preferences by id.
    """

    serializer_class = PreferencesSerializer

    def post(self, request):
        """
        Set user preferences.
        """
        preferences_data = request.data.get("preferences", [])
        if not isinstance(preferences_data, list):
            return Response(
                {"error": "preferences should be a list"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        response_data = []
        errors = []

        for preference_data in preferences_data:
            data = {
                "user": user.id,
                "preference": preference_data.capitalize(),
            }
            serializer = PreferencesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response_data.append(serializer.data)
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(
                {"created": response_data, "errors": errors},
                status=status.HTTP_207_MULTI_STATUS,
            )

        return Response(response_data, status=status.HTTP_201_CREATED)

    @method_decorator(cache_page(60 * 60 * 24))  # cache for 1 day
    def get(self, request, preference=None):
        """
        Retrieve user preferences.
        """
        user = request.user.id
        if not preference:
            instance = Preferences.objects.filter(user=user)
        else:
            try:
                instance = Preferences.objects.get(
                    user=user, preference=preference.capitalize()
                )
            except Preferences.DoesNotExist:
                return Response(
                    {"message": "no such record"}, status=status.HTTP_404_NOT_FOUND
                )

        serializer = self.serializer_class(instance, many=(not preference))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, record_id):
        """
        Update user preferences.
        """
        user = request.user.id
        try:
            instance = Preferences.objects.get(user=user, id=record_id)
        except Preferences.DoesNotExist:
            return Response(
                {"error": "No such record"}, status=status.HTTP_404_NOT_FOUND
            )
        request.data["preference"] = request.data["preference"].capitalize()
        request.data["user"] = instance.user.id
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoView(APIView):
    """
    View to manage videos.

    POST request to add a new video and GET requests to retrieve videos by category.
    """

    serializer_class = VideoSerializer

    def post(self, request):
        """
        Add a new video.
        """
        request.data["category"] = request.data["category"].capitalize()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(cache_page(60 * 60 * 24))  # cache for 1 day
    def get(self, request):
        """
        Retrieve videos by user chosen categories.
        """
        user = request.user.id
        preferences = Preferences.objects.filter(user=user).values_list(
            "preference", flat=True
        )

        videos = Video.objects.filter(
            category__in=[preference.capitalize() for preference in preferences]
        )
        serializer = self.serializer_class(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoStatisticView(APIView):
    """
    View to manage video statistics.

    POST request to add new video statistics and GET request to retrieve all statistics of video by video ID.
    """

    def post(self, request):
        """
        Add new video statistics.
        """
        user = request.user
        request.data["user"] = user.id
        request.data["interaction_type"] = request.data["interaction_type"].capitalize()

        serializer = VideoStatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(cache_page(60 * 60 * 24))  # cache for 1 day
    def get(self, request, video_id):
        """
        Retrieve video statistics by video ID.
        """
        user = request.user.id
        statistics = VideoStatistics.objects.filter(user=user, video_id=video_id)
        serializer = VideoStatisticSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoStatisticListView(APIView):
    """
    Base view to retrieve video statistics. Other classes will import this view

    Subclasses should specify the interaction type.
    """

    serializer_class = VideoStatisticSerializer
    interaction_type = None

    @method_decorator(cache_page(60 * 60 * 24))  # cache for 1 day
    def get(self, request, video_id):
        user = request.user
        queryset = VideoStatistics.objects.filter(
            user=user.id, video_id=video_id, interaction_type=self.interaction_type
        )
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoStatisticViewsListView(VideoStatisticListView):
    """
    View to retrieve a list of video views statistics.

    """

    interaction_type = "View"


class VideoStatisticSharesListView(VideoStatisticListView):
    """
    View to retrieve a list of video shares statistics.

    """

    interaction_type = "Share"


class VideoStatisticDownloadsListView(VideoStatisticListView):
    """
    View to retrieve a list of video downloads statistics.

    """

    interaction_type = "Download"
