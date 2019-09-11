from django.shortcuts import render

# Create your views here.

def index(request):
    if 'count' not in request.session:
        request.session.count = 0
    return render(request, 'first_app/index.html')

def show(request):
    request.session.count += 1
    context = {
        'name': name,
    }
    return render(request, 'first_app/show.html')
