from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django_email_sender.ems_messages.models import Message
from django.views import generic
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import random
import logging


logger = logging.getLogger(__name__)


class DetailView(generic.DetailView):
    model = Message
    template_name = 'messages/detail.html'
    context_object_name = 'message'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['user', 'source', 'destination', 'content', ]

    def clean_content(self):
        content = self.cleaned_data['content']
        logger.debug('Cleaning content field: {}'.format(content))

        if 'the' in content:
            raise ValidationError("This content is not allowed")
        else:
            return content


def index(request):

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            logger.debug('Form is valid, message is {}'.format(form.instance))
            form.instance.save()
            return HttpResponseRedirect(reverse('message:index', args=tuple()))
        else:
            logger.debug('Form is not valid: {}'.format(form.errors))

            context = create_default_context()
            context.update({'form': form, 'form_error': True})

            return render(request, 'messages/index.html', context)

    else:
        # creation test is faster by already binding form with default values
        default_message = Message(
            user=User.objects.all()[0],
            source="the source",
            destination="the dest",
            content="the content {}".format(random.randint(1, 10)))

        context = create_default_context()
        context.update({'form': MessageForm(instance=default_message), 'form_error': False})

        return render(request, 'messages/index.html', context)


def create_default_context():
    return {
        'message_list': Message.objects.order_by('-date')[:5],
    }
