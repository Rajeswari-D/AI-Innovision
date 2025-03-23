from django.db import models

class IdeaEvaluate(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Idea(models.Model):
    idea_evaluate = models.ForeignKey(IdeaEvaluate, related_name='ideas', on_delete=models.CASCADE)
    prompt = models.TextField()
    voice_input = models.FileField(upload_to='voice_inputs/', blank=True, null=True)  # Stores voice-to-text files
    document = models.FileField(upload_to='idea_documents/', blank=True, null=True)  # Stores uploaded documents
    feasibility_score = models.FloatField(blank=True, null=True)
    future_predictions = models.TextField(blank=True, null=True)
    risk_analysis = models.TextField(blank=True, null=True)
    uvp_analysis = models.TextField(blank=True, null=True)
    evaluation_score = models.IntegerField(blank=True, null=True)
    ai_feedback = models.TextField(blank=True, null=True)
    improvement_suggestions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Idea: {self.idea_evaluate.title}'
