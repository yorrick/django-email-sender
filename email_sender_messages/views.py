from django.shortcuts import render, get_object_or_404
from email_sender_messages.models import Message


def index(request):
    messages = Message.objects.order_by('-date')[:5]
    context = {'messages': messages}
    return render(request, 'messages/index.html', context)


def detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    context = {'message': message}
    return render(request, 'messages/detail.html', context)


def create(request):
    pass