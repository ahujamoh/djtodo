from django.db import models

class TodoList(models.Model):
'''
    Table in database as title, description and datetime for todo list
'''
    title = models.CharField(max_length=200, unique=True) # Title for to-do list
    description = models.TextField() # Description field for todo list
    datetime = models.DateTimeField() # Creation date tiome
  
    def __unicode__(self):
'''
    Returns title of the todo task
'''
        return self.title
