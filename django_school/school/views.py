from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Grade, Profile, Theme
from .serializers import GradeListSerializer, GradeCreateSerializer, ProfileCreateSerializer, ProfileListSerializer, \
    ProfileDetailSerializer, ThemeCreateSerializer, QuestionCreateSerializer, ThemeListSerializer, \
    ThemeQuestionsSerializer


class GradeListView(generics.ListAPIView):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all()
    filter_backends = (DjangoFilterBackend,)


class GradeCreateView(generics.CreateAPIView):
    serializer_class = GradeCreateSerializer


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileCreateSerializer


class ThemeCreateView(generics.CreateAPIView):
    serializer_class = ThemeCreateSerializer


class ThemeListView(generics.ListAPIView):
    serializer_class = ThemeListSerializer
    queryset = Theme.objects.all()
    filter_backends = (DjangoFilterBackend,)


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializer


class ThemeQuestionDetailView(generics.RetrieveAPIView):
    serializer_class = ThemeQuestionsSerializer
    queryset = Theme.objects.all()
    filter_backends = (DjangoFilterBackend,)


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()
    filter_backends = (DjangoFilterBackend,)


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    filter_backends = (DjangoFilterBackend,)
