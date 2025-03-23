from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from evaluator.analyzer import evaluate_startup_idea, generate_response

class StartupEvaluatorView(APIView):
    def post(self, request):
        idea_text = request.data.get('idea', '')
        
        if not idea_text:
            return Response(
                {'error': 'Please provide a startup idea to evaluate'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Evaluate the startup idea
        evaluation_result = evaluate_startup_idea(idea_text)
        
        # Generate response
        response_text = generate_response(evaluation_result)
        
        return Response({
            'response': response_text,
            'evaluation': evaluation_result
        })

class StartupChatView(APIView):
    def post(self, request):
        message = request.data.get('message', '')
        
        if not message:
            return Response(
                {'error': 'Please provide a message'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if the message is a startup idea or a follow-up question
        if any(keyword in message.lower() for keyword in ['my idea is', 'startup idea', 'business idea', 'new idea']):
            # Evaluate the startup idea
            evaluation_result = evaluate_startup_idea(message)
            response_text = generate_response(evaluation_result)
        else:
            # Handle follow-up questions with predefined responses
            keywords = {
                'feasibility': 'Feasibility considers factors like market need, technical complexity, and resource requirements.',
                'sentiment': 'Sentiment analysis examines how positively or negatively your idea might be received based on social media trends.',
                'historical': 'Historical success rates are derived from analyzing similar startups in your industry category.',
                'funding': 'Funding requirements vary by industry. Tech startups typically need more initial capital than service-based businesses.',
                'competition': 'Understanding your competition is crucial. Consider both direct competitors and potential substitutes.',
                'time': 'Time to market varies significantly. Simple apps can launch in months, while complex platforms might take years.',
                'team': 'Most successful startups have diverse founding teams with complementary skills.',
                'market': 'Market validation is critical. Consider conducting surveys, interviews, or creating an MVP to test your idea.',
            }
            
            for keyword, response in keywords.items():
                if keyword in message.lower():
                    response_text = response
                    break
            else:
                response_text = "I'm here to evaluate startup ideas. Could you share your startup concept so I can provide a detailed analysis?"
        
        return Response({'response': response_text})
