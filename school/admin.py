from django.contrib import admin

from .models import Grade, Student, Theme, QuestionForGrade, Question

admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Theme)
admin.site.register(QuestionForGrade)
admin.site.register(Question)