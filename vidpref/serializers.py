from rest_framework import serializers

from .models import Preferences, User, Video, VideoStatistics


class PreferencesSerializer(serializers.ModelSerializer):
    """
    Serializer for preferences.

    For serialization and deserialization of user preferences.
    """

    class Meta:
        model = Preferences
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for videos.

    For serialization and deserialization of video data.
    """

    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "category",
            "url",
        )


class VideoStatisticSerializer(serializers.ModelSerializer):
    """
    Serializer for video statistics.

    For serialization and deserialization of video statistics data.
    """

    class Meta:
        model = VideoStatistics
        fields = ["id", "video", "user", "interaction_type", "timestamp"]
