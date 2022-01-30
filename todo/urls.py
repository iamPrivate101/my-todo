from django.urls import path
from todo.views import todo_list, todo_detail

app_name = 'todo'
urlpatterns = [
    path("", todo_list, name="list"),
    path('detail/<int:pk>/',todo_detail, name='detail')
]
