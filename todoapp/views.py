from models import TodoList 
from django.shortcuts import render_to_response

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
