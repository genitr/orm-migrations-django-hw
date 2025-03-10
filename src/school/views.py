from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    ordering = 'group'

    context = {
        'object_list': Student.objects.all().order_by(ordering)
    }

    return render(request, template, context)
