from django.db import models

class TodoList(models.Model):
    '''
        Table in database as title, description and datetime for todo list
    '''
    title = models.CharField(max_length=200, unique=True) # Title for to-do list
    datetime = models.DateTimeField()                     # Creation date tiome
    priority = models.IntegerField(default=0)             # Priority of the task
    done = models.BooleanField(default=False)             # Done or not!
    description = models.TextField()                      # Description field for todo list
  
    def __unicode__(self):
        '''
            REturns todolist title
        '''
        return self.title
