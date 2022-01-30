from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)
    is_completed=models.BooleanField(default=False)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        # setting up the singular and plural name
        verbose_name = "My Todo"
        verbose_name_plural = "My Todos"
        # manage todo list in alphabetic order
        ordering = ("title", ) 

    # making the title readable into string
    def __str__(self):
        return self.title