from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.student.username}"

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    student_answer = models.TextField()
    teacher_feedback = models.TextField(blank=True, null=True)
    marks = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Answer to: {self.question.text[:30]}"
