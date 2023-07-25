from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
 

# Create your views here.
def Fee_list(request):
    return render(request ,"school_fees/")


def Fee_form(request):
    return render (request, "school_fees/")


def Fee_delete(request):
    return

