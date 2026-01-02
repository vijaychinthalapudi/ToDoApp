from django.db import models

# Create your models here.
class Todo(models.Model):
    #title of tasks
    title = models.CharField(max_length=200)
    #descriptio of the task
    description = models.TextField(blank=True)
    #status of task
    completed = models.BooleanField(default=False)
    #timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
