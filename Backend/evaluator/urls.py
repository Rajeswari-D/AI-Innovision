from django.urls import path
from .views import IdeaCreateView  # Removed IdeaEvaluateListCreateView if not needed

urlpatterns = [
    path('evaluate-idea/', IdeaCreateView.as_view(), name='evaluate-idea'),
]
