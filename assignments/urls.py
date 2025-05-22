from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import MyLoginView, signup  # ← import it

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('answer/<int:assignment_id>/', views.answer_assignment, name='answer_assignment'),
    path('results/<int:assignment_id>/', views.view_results, name='view_results'),

    # Auth paths
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'), 
    path('results/<int:assignment_id>/download/', views.download_results_pdf, name='download_results_pdf'),

]
