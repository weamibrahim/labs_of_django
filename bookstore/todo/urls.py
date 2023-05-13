from django.urls import path
from .views import index, todo_list, todo_detail, todo_delete, todo_update

app_name = 'todo'

# http://localhost:8000/post/2/comment/1
urlpatterns = [
    path('index', index, name='todo-index'),
    path('book_list/', todo_list, name="todo-list"),
    path('book_detail/<int:task_id>', todo_detail, name="todo-detail"),
    path('book_delete/<int:task_id>', todo_delete, name="todo-delete"),
    path('book_update/<int:task_id>', todo_update, name="todo-update")
]