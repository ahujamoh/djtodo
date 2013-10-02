from models import TodoList 
from django.shortcuts import render_to_response

def home(request):
    '''
        Returns all the to-do entries with all informaion to view at /
    '''
    todos = TodoList.objects.all()
    return render_to_response('home.html', {'todos': todos})
