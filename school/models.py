from datetime import date

from django.db import models


# Working version

class Profile(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Grade(models.Model):
    number = models.IntegerField()
    letter = models.CharField(max_length=1)
    # profile = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='grades')

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return f"{self.number} {self.letter} ({self.profile})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self):
        return f"{self.name} {self.grade}"


class Theme(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(default=date.today)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return f"{self.name} f{self.created_at}"


class Question(models.Model):
    name = models.TextField()
    created_at = models.DateField(default=date.today)
    image_file = models.ImageField(upload_to="question_images/", default=None)
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='questions')
    # grades = models.ManyToManyField(Grade, through='QuestionForGrade')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"{self.name} {self.theme} {self.grades}"


class QuestionForGrade(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, default=None)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    deadline = models.DateField(default=date.today)

    class Meta:
        unique_together = ('theme', 'grade')
        verbose_name = 'Вопрос для классы'
        verbose_name_plural = "Вопросы для класса"

    def __str__(self):
        return f"{self.theme} {self.grade} {self.deadline}"


class StudentJournal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.TextField(default=None, null=True)
    correct = models.BooleanField(default=None, null=True)
    score = models.IntegerField(default=None, null=True)
    date = models.DateField(default=date.today)

    class Meta:
        unique_together = ('student', 'question')
        verbose_name = 'Журнал студента'
        verbose_name_plural = "Журнал студентов"

    def __str__(self):
        return f"{self.student} {self.question} {self.score} {self.date}"
