from django.urls import path

from . import views

app_name = 'simplemesh'
urlpatterns = [
	# /
	path('', views.IndexView.as_view(), name='index'),

	# /1
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

	# /message/1
	path('message/<int:pk>', views.MessageView.as_view(), name='message'),

	# /start [to start conversation]
	path('start/', views.start, name='start'),

	# /1/addmessage
	path('<int:conversation_id>/addmessage', views.add_message, name='add_message'),

	# /message/1/thought
	path('message/<int:message_id>/thought', views.add_thought, name='add_thought'),

	# /search/text%ssearch
	path('search/', views.search, name='search')
]
