# from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Grade, Profile, Theme, Question, QuestionForGrade, StudentJournal, Student
from .serializers import GradeListSerializer, GradeCreateSerializer, ProfileCreateSerializer, ProfileListSerializer, \
    ProfileDetailSerializer, ThemeCreateSerializer, QuestionCreateSerializer, ThemeListSerializer, \
    ThemeQuestionsSerializer, GradeDestroySerializer, ProfileDestroySerializer, QuestionDestroySerializer, \
    ThemeDestroySerializer, QuestionUpdateSerializer, ProfileUpdateSerializer, GradeUpdateSerializer, \
    ThemeUpdateSerializer, QuestionForGradeCreateSerializer, AnswerQuestionSerializer, StudentCreateSerializer, \
    GradeStudentsSerializer, QuestionForGradeSerializer, QuestionByUserIdSerializer, QuestionForGradeSerializerByUserId, \
    StudentImageSerializer


class GradeListView(generics.ListAPIView):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all()

    def get(self, request, *args, **kwargs):
        num = request.query_params["num"]
        if num is not None:
            if num == 'all':
                grade_list = Grade.objects.all()
            else:
                grade_list = Grade.objects.filter(number=num)

            serializer = GradeListSerializer(grade_list, many=True)
        return Response(serializer.data)
    # filter_backends = (DjangoFilterBackend,)


class ThemeForGrade(generics.ListAPIView):
    serializer_class = QuestionForGradeSerializer
    queryset = QuestionForGrade.objects.all()

    def get(self, request, *args, **kwargs):
        number = request.query_params["num"]
        letter = request.query_params["letter"]
        if number is not None and letter is not None:
            grade = Grade.objects.get(number=number, letter=letter)
            grade_id = grade.pk
            questions_for_grade_list = QuestionForGrade.objects.filter(grade_id=grade_id)
            serializer = QuestionForGradeSerializer(questions_for_grade_list, many=True)
        return Response(serializer.data)


class ThemeByUserId(generics.ListAPIView):
    serializer_class = QuestionForGradeSerializerByUserId
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        userId = request.query_params["userId"]
        if userId is not None:
            student = Student.objects.get(userId=userId)
            grade_id = student.grade.pk
            themes = QuestionForGrade.objects.filter(grade_id=grade_id)
            serializer = QuestionForGradeSerializerByUserId(themes, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'userId not found'})


class GradeDetailView(generics.ListAPIView):
    serializer_class = GradeListSerializer
    queryset = Grade.objects.all()

    def get(self, request, *args, **kwargs):
        number = request.query_params["num"]
        letter = request.query_params["letter"]
        if number is not None and letter is not None:
            grade_info = Grade.objects.get(number=number, letter=letter)
            if grade_info is not None:
                serializer = GradeListSerializer(grade_info)
                return Response(serializer.data)
            else:
                Response(None)


# class GradeAPIView(APIView):
#     serializer_class = GradeListSerializer
#     queryset = Grade.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         num = request.query_params["num"]
#         if num != None:
#             if num == 'all':
#                 grade_list = Grade.objects.all()
#                 serializer = GradeListSerializer(grade_list, many=True)
#             else:
#                 grade_list = Grade.objects.filter(number=num)
#                 serializer = GradeListSerializer(grade_list, many=True)
#         return Response(serializer.data)


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


class StudentCreateViewImage(FlexFieldsModelViewSet):
    serializer_class = StudentImageSerializer
    queryset = Student.objects.all()
