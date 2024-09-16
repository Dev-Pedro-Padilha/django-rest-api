from django.urls import path
from api.views import MessageListCreate, MessageRetrieveUpdateDestroy, TaskListCreate, TaskRetrieveUpdateDestroy

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Endpoints para mensagens
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroy.as_view(), name='message-detail'),

    # Endpoints para tarefas
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
