from django.db import models
from django.utils import timezone

class Conversation(models.Model):
    text = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')

    def __str__(self):
        return self.text

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date sent')
    def __str__(self):
        return self.text

class Thought(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date sent')
    def __str__(self):
        return self.text
