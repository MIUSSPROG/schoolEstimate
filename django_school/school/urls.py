from django.urls import path

from . import views

urlpatterns = [
    path("grades/", views.GradeListView.as_view()),
    path("grade/", views.GradeCreateView.as_view()),
    path("profile/", views.ProfileCreateView.as_view()),
    path("profiles/", views.ProfileListView.as_view()),
    path("profile/<int:pk>/", views.ProfileDetailView.as_view()),
]
