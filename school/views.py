# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Grade, Profile, Theme, Question, QuestionForGrade, StudentJournal, Student
from .serializers import GradeListSerializer, GradeCreateSerializer, ProfileCreateSerializer, ProfileListSerializer, \
    ProfileDetailSerializer, ThemeCreateSerializer, QuestionCreateSerializer, ThemeListSerializer, \
    ThemeQuestionsSerializer, GradeDestroySerializer, ProfileDestroySerializer, QuestionDestroySerializer, \
    ThemeDestroySerializer, QuestionUpdateSerializer, ProfileUpdateSerializer, GradeUpdateSerializer, \
    ThemeUpdateSerializer, QuestionForGradeCreateSerializer, AnswerQuestionSerializer, StudentCreateSerializer, \
    GradeStudentsSerializer, GradeParamSerializer


class GradeListView(generics.ListAPIView):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all()
    # filter_backends = (DjangoFilterBackend,)


class GradeAPIView(APIView):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all()

    def get(self, request, *args, **kwargs):
        num = request.query_params["num"]
        if num != None:
            grade_list = Grade.objects.filter(number=num)
            serializer = GradeListSerializer(grade_list, many=True)
        else:
            grade_list = Grade.objects.all()
            serializer = GradeListSerializer(grade_list, many=True)
        return Response(serializer.data)


class GradeCreateView(generics.CreateAPIView):
    serializer_class = GradeCreateSerializer


class GradeDeleteView(generics.DestroyAPIView):
    serializer_class = GradeDestroySerializer
    queryset = Grade.objects.all()


class GradeUpdateView(generics.UpdateAPIView):
    serializer_class = GradeUpdateSerializer
    queryset = Grade.objects.all()


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileCreateSerializer


class ProfileDeleteView(generics.DestroyAPIView):
    serializer_class = ProfileDestroySerializer
    queryset = Profile.objects.all()


class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()


class ThemeUpdateView(generics.UpdateAPIView):
    serializer_class = ThemeUpdateSerializer
    queryset = Theme.objects.all()


class ThemeDeleteView(generics.DestroyAPIView):
    serializer_class = ThemeDestroySerializer
    queryset = Theme.objects.all()


class ThemeCreateView(generics.CreateAPIView):
    serializer_class = ThemeCreateSerializer


class ThemeListView(generics.ListAPIView):
    serializer_class = ThemeListSerializer
    queryset = Theme.objects.all()
    # filter_backends = (DjangoFilterBackend,)


class QuestionUpdateView(generics.UpdateAPIView):
    serializer_class = QuestionUpdateSerializer
    queryset = Question.objects.all()


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionCreateSerializer


class QuestionDeleteView(generics.DestroyAPIView):
    serializer_class = QuestionDestroySerializer
    queryset = Question.objects.all()


class QuestionForGradeCreateView(generics.CreateAPIView):
    serializer_class = QuestionForGradeCreateSerializer
    queryset = QuestionForGrade.objects.all()


class ThemeQuestionDetailView(generics.RetrieveAPIView):
    serializer_class = ThemeQuestionsSerializer
    queryset = Theme.objects.all()
    # filter_backends = (DjangoFilterBackend,)


class GradeStudentsDetailView(generics.RetrieveAPIView):
    serializer_class = GradeStudentsSerializer
    queryset = Grade.objects.all()


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileListSerializer
    queryset = Profile.objects.all()
    # filter_backends = (DjangoFilterBackend,)


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    # filter_backends = (DjangoFilterBackend,)


class AnswerQuestionView(generics.CreateAPIView):
    serializer_class = AnswerQuestionSerializer
    queryset = StudentJournal.objects.all()


class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentCreateSerializer
    queryset = Student.objects.all()
