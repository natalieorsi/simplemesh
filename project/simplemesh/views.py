from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Conversation, Message

class IndexView(generic.ListView):
	template_name='simplemesh/index.html'
	context_object_name = 'results'

	def get_queryset(self):
		return Conversation.objects.order_by('start_date')

class DetailView(generic.DetailView):
	model = Conversation
	template_name = "simplemesh/detail.html"

class MessageView(generic.DetailView):
	model = Message
	template_name = 'simplemesh/message.html'

def start(request):
	if 'new' in request.POST:
		text = request.POST['new']
		time = timezone.now()
		c = Conversation(text=text, start_date=time)
		c.save()

	else:
		print("error, no text provided")
	return HttpResponseRedirect(reverse('simplemesh:index'))

def add_message(request, conversation_id):
	c = get_object_or_404(Conversation, pk=conversation_id)
	if 'new' in request.POST:	
		text = request.POST['new']
		time = timezone.now()
		c.message_set.create(text=text, pub_date=time)	

	return HttpResponseRedirect(reverse('simplemesh:detail',
	args=(conversation_id,)))

def add_thought(request, message_id):
	if 'new' in request.POST:
		m = get_object_or_404(Message, pk=message_id)
		text = request.POST['new']
		time = timezone.now()
		m.thought_set.create(text=text, pub_date=time)

	return HttpResponseRedirect(reverse('simplemesh:message',
	args=(message_id,)))

def search(request): 
	queried = "query" in request.POST
	query = request.POST['query'] if queried else ''
	object_type_input = request.POST['object_type'] if 'object_type' in request.POST else None
	object_type = Message if object_type_input == "Message" else Conversation
	no_results_text = "No results for your query." 
	errors = []
	result = None

	try:
		if query:
			result = object_type.objects.filter(text__icontains=query)
	
			if not result:
				errors.append(no_results_text)

	# TODO would be to create messaging and error handling

	except Exception as e:
		return HttpResponseRedirect(reverse('simplemesh:index'))

	context = {"type": object_type.__name__, 
		"errors": errors, "results": result}

	print(f"Queried: {queried}")
	return render(request, 'simplemesh/search.html', context)
