
from django.shortcuts import render

def messages_view(request):
    return render(request, 'messages.html')
