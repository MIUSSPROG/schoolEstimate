from rest_framework import serializers

from .models import Grade, Profile


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
