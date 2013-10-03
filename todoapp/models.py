from django.db import models
from django.contrib import admin

class TodoList(models.Model):
    '''
        Table in database as title, description and datetime for todo list
    '''
    priority_tuple = (
        ('Little', 'Little'),
        ('Normal', 'Normal'),
        ('Important', 'Important'),
    )
    status_tuple = (
        ('Done', 'Done'),
        ('Pending', 'Pending'),
    )
    title = models.CharField(max_length=200)                                 # Title for to-do list
    datetime = models.DateTimeField()                                        # Creation date tiome
    priority = models.CharField(max_length=10, choices=priority_tuple, default='Normal')        # Priority of the task
    status = models.CharField(max_length=10, choices=status_tuple, default='Pending')           # Done or not!
  
    def __unicode__(self):
        '''
            REturns todolist title
        '''
        return self.title

admin.site.register(TodoList)
