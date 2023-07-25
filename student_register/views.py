from django.shortcuts import render

# Create your views here.
def student_list(request):
    return render(request ,"student_register")


def student_form(request):

    return render (request, "student_register",)


def student_delete(request):
    return

