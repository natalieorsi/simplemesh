import datetime
from django.http import request
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.utils import timezone

from .models import Conversation, Message, Thought
from .views import search
# Run tests by navigating to manage.py and running `python manage.py test simplemesh`

class AllTests(TestCase):
    def test_create_conversation(self):
        now = timezone.now()
        text = "Auto test: Creating a conversation"
        c = Conversation(start_date=now, text=text)
        c.save()
        retrieved_type = type(get_object_or_404(Conversation, id=c.id))

        self.assertIs(retrieved_type, Conversation)
  
    def test_create_message(self):
        now = timezone.now()

        c = Conversation.objects.create(
            start_date=now,
            text = "Auto test: Creating a conversation"
        )
        c.save()

        m=c.message_set.create(
            pub_date=now,
            text = "Auto test: Creating a message"
        )
        m.save()
        retrieved_type = type(get_object_or_404(Message, id=m.id))
    
        # if I had more time I would clean up all these test data after the assert
        self.assertIs(retrieved_type,Message)
  
    def test_create_thought(self):
        now = timezone.now()

        c = Conversation.objects.create(
            start_date=now,
            text = "Auto test: Creating a conversation"
        )
        c.save()

        m=c.message_set.create(
            pub_date=now,
            text = "Auto test: Creating a message"
        )
        m.save()

        t=m.thought_set.create(
            pub_date=now,
            text = "Auto test: Creating a thought"
        )
        t.save()
        
        retrieved_type = type(get_object_or_404(Thought, id=t.id))
        self.assertIs(retrieved_type,Thought)
        
    # other tests if I had the time:
    # test empty string input for each type of model
    # test future date input for start_date, pub_date
    # test escape behavior by submitting queries with HTML and python
