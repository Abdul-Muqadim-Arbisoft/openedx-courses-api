from django.shortcuts import render


def hello_template(request):
    return render(request, 'courses_api/hello.html')
