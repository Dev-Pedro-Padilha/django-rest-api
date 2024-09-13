from rest_framework import generics
from .models import Message, Task
from .serializers import MessageSerializer, TaskSerializer

#############################################################################################
#Messsage#
class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
# View para obter, atualizar ou deletar uma mensagem específica
class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
#############################################################################################

#############################################################################################
#Task#
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View para obter, atualizar ou deletar uma tarefa específica
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
#############################################################################################