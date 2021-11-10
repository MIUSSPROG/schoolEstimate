from rest_framework import serializers

from .models import Grade, Profile, Theme, Question


class GradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('number', 'letter', 'grade_profile')

    grade_profile = serializers.SerializerMethodField('get_grade_profile')

    def get_grade_profile(self, obj):
        return obj.profile.name


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


class GradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ThemeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class ThemeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'created_at', 'image_file')


class ThemeQuestionsSerializer(serializers.ModelSerializer):
    questions = ThemeQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'questions')
