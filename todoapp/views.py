from models import TodoList 
from django.shortcuts import render_to_response, render

def home(request):
    '''
        Returns all the to-do entries with all informaion to view at /
    '''
    todos = TodoList.objects.all()
    return render_to_response('home.html', {'todos': todos})

def stats(request):
    '''
        Returns count how many tasks are pending, how many completed
    '''
    todos = TodoList.objects.all()
    pending = 0
    completed = 0
    for todo in todos:
        if todo.status == 'Pending':
            pending += 1
        else:
            completed += 1
    try:
        pendper = (float(pending)/(pending+completed))*100
    except ZeroDivisionError:
        pendper = 0
    compper = 100 - pendper
    pcstats = {
        "pending": pending,
        "completed": completed,
        "pendper": "%0.2f" %(pendper),
        "compper": "%0.2f" %(compper)
    }
    return render_to_response('stats.html', {'stats' : pcstats})

def search(request):
    try:
        search_term = request.GET['search']
        if not search_term in ["", " "]:
            results = TodoList.objects.filter(title__contains=search_term)|TodoList.objects.filter(status__contains=search_term)|TodoList.objects.filter(priority__contains=search_term)|TodoList.objects.filter(datetime__contains=search_term)
        return render(request, 'search.html', {'results':results})
    except:
        return render(request, 'search.html')
