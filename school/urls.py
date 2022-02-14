from django.urls import path

from . import views

urlpatterns = [
    path("grades/", views.GradeListView.as_view()),
    path("grade/", views.GradeCreateView.as_view()),
    path("grade/<int:pk>/", views.GradeDeleteView.as_view()),
    path("grade/update/<int:pk>/", views.GradeUpdateView.as_view()),
    path("grade_id/", views.GradeDetailView.as_view()),
    path("profile/", views.ProfileCreateView.as_view()),
    path("profiles/", views.ProfileListView.as_view()),
    path("profile/<int:pk>/", views.ProfileDetailView.as_view()),
    path("profile/update/<int:pk>/", views.ProfileUpdateView.as_view()),
    path("profile/delete/<int:pk>/", views.ProfileDeleteView.as_view()),
    path("theme/", views.ThemeCreateView.as_view()),
    path("themes/", views.ThemeListView.as_view()),
    path("theme/delete/<int:pk>/", views.ThemeDeleteView.as_view()),
    path("theme/update/<int:pk>/", views.ThemeUpdateView.as_view()),
    path("themes_for_grade/", views.ThemeForGrade.as_view()),
    path("question/", views.QuestionCreateView.as_view()),
    path("question/update/<int:pk>/", views.QuestionUpdateView.as_view()),
    path("question/<int:pk>/", views.QuestionDeleteView.as_view()),
    path("theme/<int:pk>/", views.ThemeQuestionDetailView.as_view()),
    path("question_for_class/", views.QuestionForGradeCreateView.as_view()),
    path("answer_question/", views.AnswerQuestionView.as_view()),
    path("student/", views.StudentCreateViewImage.as_view({'post': 'create'})),
    path("students_of_grade/<int:pk>", views.GradeStudentsDetailView.as_view()),
    path("question_by_userId/", views.ThemeByUserId.as_view())
]
