import datetime
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.utils import timezone

from .models import Conversation, Message, Thought

# Run tests by navigating to manage.py and running `python manage.py test simplemesh`

class ConversationModelTests(TestCase):
    def test_create_conversation(self):
        now = timezone.now()
        text = "Auto test: Creating a conversation"
        c = Conversation(start_date=now, text=text)
        c.save()
        retrieved_type = type(get_object_or_404(Conversation, id=c.id))

        self.assertIs(retrieved_type, Conversation)
  
    def test_create_message(self):
        
          # Assuming ID 1 exists; in reality it would be preferable to search and select 
         # a conversation to add to, or create one in the test
        now = timezone.now()

        c = Conversation.objects.create(
            
        )
        c.start_date = c.startdate if c.startdate else now
        c.text = c.text if c.text else "Auto test: Creating a conversation"
  
        text = "Auto test: Creating a message"
        m=c.message_set.create(text=text, pub_date=now)
        c.save()
        m.save()
        retrieved_type = type(get_object_or_404(Message, id=m.id))
    
        # if I had more time I would clean up all these test data after the assert
        self.assertIs(type(retrieved_type),Message)
  
    def test_create_thought(self):
          # Assuming ID 1 exists; in reality it would be preferable to search and select 
         # a message to add to, or create one in the test
        now = timezone.now()
        text = "Auto test: Creating a thought"
        m = get_object_or_404(Message, id=1)
        t=m.thought_set.create(text=text, pub_date=now)
        retrieved_type = type(get_object_or_404(Thought, id=t.id))
        self.assertIs(type(retrieved_type),Thought)
        
    # other tests if I had the time:
    # test empty string input for each type of model
    # test future date input for start_date, pub_date
    # test escape behavior by submitting queries with HTML and python
