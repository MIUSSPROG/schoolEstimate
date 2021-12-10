from rest_framework import serializers

from .models import Grade, Profile, Theme, Question, QuestionForGrade, StudentJournal, Student


# class GradeListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Grade
#         fields = ('id', 'number', 'letter', 'grade_profile')
#
#     grade_profile = serializers.SerializerMethodField('get_grade_profile')
#
#     def get_grade_profile(self, obj):
#         return obj.profile.name


class GradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class GradeDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class GradeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileGradeList(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('number', 'letter')


class ProfileDetailSerializer(serializers.ModelSerializer):
    grades = ProfileGradeList(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'grades')


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ThemeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class ThemeDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class ThemeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class QuestionByUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name')


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class QuestionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionForGradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionForGrade
        fields = "__all__"


class ThemeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'created_at', 'image_file')


class ThemeQuestionsSerializer(serializers.ModelSerializer):
    questions = ThemeQuestionSerializer(many=True, read_only=True)

    class Meta:
        # model = Profile
        model = Theme
        fields = ('name', 'questions')


class GradeStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'userId')


class QuestionForGradeSerializer(serializers.ModelSerializer):
    # themes = ThemeListSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionForGrade
        fields = ('theme_id', 'deadline', 'theme_name')

    theme_name = serializers.SerializerMethodField('get_theme_names')

    def get_theme_names(self, obj):
        return obj.theme.name


class QuestionForGradeSerializerByUserId(serializers.ModelSerializer):
    questions = QuestionByUserIdSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionForGrade
        fields = ('theme_id', 'deadline', 'theme_name', 'questions')

    theme_name = serializers.SerializerMethodField('get_theme_names')

    def get_theme_names(self, obj):
        return obj.theme.name


class GradeStudentsSerializer(serializers.ModelSerializer):
    students = GradeStudentSerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = ('number', 'letter', 'grade_profile', 'students')

    grade_profile = serializers.SerializerMethodField('get_grade_profile')

    def get_grade_profile(self, obj):
        return obj.profile.name


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentJournal
        fields = "__all__"


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class GradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'number', 'letter', 'grade_profile')

    grade_profile = serializers.SerializerMethodField('get_grade_profile')

    def get_grade_profile(self, obj):
        return obj.profile.name
