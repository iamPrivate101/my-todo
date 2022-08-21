from django.urls import path
from todo.views import index,todo_list, todo_detail, todo_create, todo_delete, todo_update


app_name = 'todo'
urlpatterns = [
    path('',index,name='index'),
    path("todo/", todo_list, name="list"),
    path('detail/<int:pk>/',todo_detail, name='detail'),
    path('delete/<int:pk>/',todo_delete, name='delete'),
    path('update/<int:pk>/',todo_update, name='update'),
    path('create/',todo_create, name='create'),
   

]
