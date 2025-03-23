import google.generativeai as genai
import os
import re
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Set Google Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Ensure API key is set

# SSL Certificate Path
CERT_PATH = r"C:\Users\rajes\OneDrive\Desktop\AI\Backend\env\Lib\site-packages\certifi\cacert.pem"

class IdeaCreateView(APIView):
    """
    View to handle idea evaluation using Google Gemini API.
    """

    def get(self, request, *args, **kwargs):
        """Handles GET request (optional message)."""
        return Response({"message": "Use POST to submit an idea for evaluation."}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handles POST request for idea evaluation."""
        user_message = request.data.get('idea')

        if not user_message:
            return Response({"error": "Idea description is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call Google Gemini API with a structured prompt
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            prompt = (
                f"""
                Evaluate the feasibility of the following startup idea:
                
                **Idea:** {user_message}
                
                ### Provide the following:
                1. Feasibility Score: A number from 0 to 100 based on market demand, technical viability, and financial sustainability.
                2. Three Key Suggestions: Actionable improvements that can make the idea stronger, focused on business strategy, innovation, or technical execution.
                3. Potential Challenges: Key obstacles the idea might face and how to overcome them.
                4. Real-time Market Analysis: A brief summary of current market trends and demand related to this idea.
                
                Ensure that the response is structured clearly and given as plain text.
                """
            )

            response = model.generate_content(prompt)
            response_text = response.text
            
            feasibility_score = self.extract_feasibility_score(response_text)
            suggestions = self.extract_suggestions(response_text)
            challenges = self.extract_challenges(response_text)
            market_analysis = self.extract_market_analysis(response_text)
            
            return Response({
                "feasibilityScore": feasibility_score,
                "suggestions": self.clean_text(suggestions),
                "challenges": challenges,
                "marketAnalysis": market_analysis
            }, status=status.HTTP_200_OK)

        except requests.exceptions.SSLError as ssl_error:
            return Response({"error": f"SSL Error: {str(ssl_error)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def extract_feasibility_score(self, text):
        """
        Extracts the feasibility score from AI response.
        """
        match = re.search(r"(\d{1,3})\s*/?\s*100", text)
        return max(0, min(100, int(match.group(1)))) if match else 50  # Default to 50 if not found

    def extract_suggestions(self, text):
        """
        Extracts up to 3 concise suggestions from AI response.
        """
        matches = re.findall(r"\d+\.\s*(.+)", text) or re.findall(r"-\s*(.+)", text)
        return matches[:3] if matches else ["No specific suggestions provided."]

    def extract_challenges(self, text):
        """
        Extracts potential challenges mentioned in the AI response.
        """
        match = re.search(r"Challenges:\s*(.+)", text, re.DOTALL)
        return match.group(1).strip() if match else "No challenges mentioned."

    def extract_market_analysis(self, text):
        """
        Extracts real-time market analysis from AI response.
        """
        match = re.search(r"Market Analysis:\s*(.+)", text, re.DOTALL)
        return match.group(1).strip() if match else "No market analysis available."

    def clean_text(self, texts):
        """
        Cleans text by removing special characters while preserving spaces and words.
        """
        return [re.sub(r'[^a-zA-Z0-9.,\s]', '', text).strip() for text in texts]