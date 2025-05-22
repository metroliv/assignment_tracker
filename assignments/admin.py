from django.contrib import admin
from .models import Course, Assignment, Question, Answer

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('title', 'student__username')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'assignment', 'text')
    search_fields = ('text',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'student_answer', 'marks')
    search_fields = ('student_answer', 'teacher_feedback')
    list_filter = ('marks',)
