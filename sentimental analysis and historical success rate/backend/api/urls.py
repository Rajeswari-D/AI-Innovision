from django.urls import path
from .views import StartupEvaluatorView, StartupChatView

urlpatterns = [
    path('evaluate/', StartupEvaluatorView.as_view(), name='evaluate'),
    path('chat/', StartupChatView.as_view(), name='chat'),
]