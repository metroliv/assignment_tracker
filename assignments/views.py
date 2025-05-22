from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment, Question, Answer, Course
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.template.loader import get_template
from django.http import HttpResponse
import weasyprint 




# Assignment creation (Teacher or Student can create)
@login_required
def create_assignment(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        course_id = request.POST['course']
        questions = request.POST.getlist('questions[]')

        course = get_object_or_404(Course, id=course_id)
        assignment = Assignment.objects.create(
            student=request.user,
            title=title,
            course=course
        )

        for q in questions:
            if q.strip():  # avoid empty questions
                Question.objects.create(assignment=assignment, text=q.strip())

        return redirect('answer_assignment', assignment_id=assignment.id)

    return render(request, 'assignments/create_assignment.html', {'courses': courses})


# Student answers the questions for a given assignment
@login_required
def answer_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == 'POST':
        # Save or update answers (avoid duplicates)
        for question in assignment.questions.all():
            answer_text = request.POST.get(f'answer_{question.id}')
            if answer_text is not None:
                answer, created = Answer.objects.update_or_create(
                    question=question,
                    defaults={'student_answer': answer_text}
                )
        return redirect('view_results', assignment_id=assignment.id)

    return render(request, 'assignments/answer_assignment.html', {'assignment': assignment})


# View assignment results including answers and feedback
@login_required
def view_results(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    return render(request, 'assignments/view_results.html', {'assignment': assignment})


# List all assignments (for teacher or student)
@login_required
def assignment_list(request):
    # If you want to restrict by user, filter here, e.g. assignments for current user
    assignments = Assignment.objects.all().order_by('-created_at')
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})




class MyLoginView(LoginView):
    template_name = 'registration/login.html'  # or wherever your template is
    authentication_form = CustomLoginForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def download_results_pdf(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    template = get_template('results_pdf.html')
    html = template.render({'assignment': assignment})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{assignment.title}_results.pdf"'

    weasyprint.HTML(string=html).write_pdf(response)
    return response
