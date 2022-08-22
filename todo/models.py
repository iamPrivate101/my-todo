from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    is_completed=models.BooleanField(default=False)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        # setting up the singular and plural name
        verbose_name = "My Todo"
        verbose_name_plural = "My Todos"
        # manage todo list in alphabetic order
        ordering = ("-created_at", ) 

    # making the title readable into string
    def __str__(self):
        return self.title
