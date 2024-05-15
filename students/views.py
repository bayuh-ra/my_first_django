from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import StudentForm
from .models import Student


# Create your views here.
def home(request): 
    if request.method == "POST":    
        form = StudentForm(request.POST)
        if form.is_valid(): 
            student = Student.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                course=form.cleaned_data["course"],
                gender=form.cleaned_data["gender"],
                age=form.cleaned_data["age"],
            )  
            return redirect('student_table')  # Redirect to the student table page after successful submission

    form = StudentForm()
    context = {"form": form}
    return render(request, 'student_form.html', context)
###############################################################################################################
def student_table(request):
    data = Student.objects.all()
    return render(request, 'student_table.html', {'data': data})
###############################################################################################################     
def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
###############################################################################################################
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.course = form.cleaned_data['course']
            student.gender = form.cleaned_data['gender']
            student.age = form.cleaned_data['age']
            student.save()
            return redirect('student_table')
    else:
        form = StudentForm(initial={
            'first_name': student.first_name,
            'last_name': student.last_name,
            'course': student.course,
            'gender': student.gender,
            'age': student.age
        })
    return render(request, 'student_form.html', {'form': form})

