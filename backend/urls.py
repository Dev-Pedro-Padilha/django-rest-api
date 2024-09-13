from django.urls import path
from api.views import MessageListCreate, MessageRetrieveUpdateDestroy, TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    # Endpoints para mensagens
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroy.as_view(), name='message-detail'),

    # Endpoints para tarefas
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]
