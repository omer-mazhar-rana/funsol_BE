from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username, email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"

    class Meta:
        indexes = [
            models.Index(fields=["username"]),
            models.Index(fields=["email"]),
        ]


class Preferences(models.Model):
    GENRES = (
        ("News", "News"),
        ("Comedy", "Comedy"),
        ("Infotainment", "Infotainment"),
        ("Entertainment", "Entertainment"),
        ("Romance", "Romance"),
        ("Tech", "Tech"),
        ("SciFi", "SciFi"),
        ("Movies", "Movies"),
        ("Thriller", "Thriller"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    preference = models.CharField(
        max_length=20, choices=GENRES, unique=True, db_index=True
    )

    def __str__(self):
        return self.preference

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["preference"]),
        ]


class Video(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50, choices=Preferences.GENRES, db_index=True
    )
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=["category"]),
        ]


class VideoStatistics(models.Model):
    VIDEO_INTERACTION_CHOICES = [
        ("View", "View"),
        ("Share", "Share"),
        ("Download", "Download"),
    ]

    video = models.ForeignKey(Video, on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, db_index=True
    )
    interaction_type = models.CharField(
        max_length=50, choices=VIDEO_INTERACTION_CHOICES, db_index=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.interaction_type} on {self.video.title} by {self.user}"

    class Meta:
        indexes = [
            models.Index(fields=["video"]),
            models.Index(fields=["user"]),
            models.Index(fields=["interaction_type"]),
            models.Index(fields=["timestamp"]),
        ]
