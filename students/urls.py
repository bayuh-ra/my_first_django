from django.urls import path

from . import views

#urlpatterns = [
    #path('', views.home),
    #path('', views.home, name='home'),
    #path('student_table/', views.student_table, name='student_table'),
    #path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    #path('delete/<int:student_id>/', views.delete_student, name='delete_student'),#new
    #path('update/<int:student_id>/', views.update_student, name='update_student'),#new
    
#]

urlpatterns = [
    path('', views.home, name='home'),
    path('student_table/', views.student_table, name='student_table'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
]