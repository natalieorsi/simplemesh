import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Conversation

# Run tests by navigating to manage.py and running `python manage.py test simplemesh`


class ConversationModelTests(TestCase):
	def test_future_conversation(self):
		now = timezone.now()
		time = datetime.timedelta(days=90) + now
		future_convo = Conversation(start_date=time)

		self.assertIs(future_convo.start_date, now)
