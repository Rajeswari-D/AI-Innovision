# backend/evaluator/analyzer.py

import re
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

from .mock_data import (
    SOCIAL_MEDIA_SENTIMENT, 
    HISTORICAL_SUCCESS_RATES, 
    DEFAULT_SENTIMENT, 
    DEFAULT_SUCCESS_RATE,
    FEASIBILITY_FACTORS
)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Preprocess text by tokenizing, removing stopwords, and lemmatizing."""
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return tokens

def categorize_idea(text):
    """Determine the category of the startup idea."""
    tokens = preprocess_text(text)
    
    # Simple keyword matching for categories
    categories = {
        "tech": ["software", "app", "platform", "tech", "digital", "ai", "machine learning", "automation", "blockchain", "saas"],
        "food": ["food", "restaurant", "delivery", "meal", "grocery", "cooking", "catering", "nutrition"],
        "health": ["health", "medical", "wellness", "fitness", "healthcare", "therapy", "doctor", "patient", "hospital"],
        "education": ["education", "learning", "teaching", "school", "student", "course", "training", "skill"],
        "finance": ["finance", "banking", "payment", "investment", "insurance", "loan", "credit", "financial"],
        "ecommerce": ["ecommerce", "retail", "shop", "store", "marketplace", "selling", "buying", "consumer"]
    }
    
    # Count occurrences of category keywords
    category_scores = {category: 0 for category in categories}
    
    for token in tokens:
        for category, keywords in categories.items():
            if token in keywords:
                category_scores[category] += 1
    
    # Find the category with the highest score
    if any(category_scores.values()):
        best_category = max(category_scores, key=category_scores.get)
        return best_category
    
    # If no clear category, use text similarity to determine the closest category
    text_str = " ".join(tokens)
    category_texts = {category: " ".join(keywords) for category, keywords in categories.items()}
    
    vectorizer = CountVectorizer().fit([text_str] + list(category_texts.values()))
    text_vector = vectorizer.transform([text_str]).toarray()[0]
    
    similarity_scores = {}
    for category, category_text in category_texts.items():
        category_vector = vectorizer.transform([category_text]).toarray()[0]
        # Simple cosine similarity
        dot_product = sum(a*b for a, b in zip(text_vector, category_vector))
        magnitude1 = sum(a*a for a in text_vector) ** 0.5
        magnitude2 = sum(b*b for b in category_vector) ** 0.5
        
        if magnitude1 * magnitude2 == 0:
            similarity_scores[category] = 0
        else:
            similarity_scores[category] = dot_product / (magnitude1 * magnitude2)
    
    best_category = max(similarity_scores, key=similarity_scores.get)
    return best_category

def analyze_sentiment(idea_text, category):
    """Analyze sentiment based on mock social media data."""
    tokens = preprocess_text(idea_text)
    
    # Get sentiment data for the category or default if not found
    sentiment_data = SOCIAL_MEDIA_SENTIMENT.get(category, DEFAULT_SENTIMENT)
    
    # Count positive and negative sentiment words
    positive_count = sum(1 for token in tokens if token in sentiment_data["positive"])
    negative_count = sum(1 for token in tokens if token in sentiment_data["negative"])
    
    # Add randomness for demo purposes
    positive_count += random.randint(1, 5)
    negative_count += random.randint(1, 3)
    
    # Calculate sentiment score
    total = positive_count + negative_count
    if total == 0:
        return {
            "score": 0.5,
            "positive_aspects": sentiment_data["positive"][:3],
            "negative_aspects": sentiment_data["negative"][:2],
            "overall": "neutral"
        }
    
    sentiment_score = positive_count / total
    
    # Determine overall sentiment
    if sentiment_score > 0.7:
        overall = "very positive"
    elif sentiment_score > 0.55:
        overall = "positive"
    elif sentiment_score > 0.45:
        overall = "neutral"
    elif sentiment_score > 0.3:
        overall = "negative"
    else:
        overall = "very negative"
    
    return {
        "score": round(sentiment_score, 2),
        "positive_aspects": sentiment_data["positive"][:3],
        "negative_aspects": sentiment_data["negative"][:2],
        "overall": overall
    }

def get_historical_data(category):
    """Get historical success data for the given category."""
    return HISTORICAL_SUCCESS_RATES.get(category, DEFAULT_SUCCESS_RATE)

def evaluate_feasibility(idea_text):
    """Evaluate the feasibility of the startup idea."""
    tokens = preprocess_text(idea_text)
    
    # Count words to estimate complexity
    complexity = min(len(set(tokens)) / max(len(tokens), 1), 1.0)
    
    # Generate random feasibility scores for demo purposes
    feasibility_scores = {}
    for factor in FEASIBILITY_FACTORS:
        # Generate a score between 0.3 and 0.9
        score = round(random.uniform(0.3, 0.9), 2)
        feasibility_scores[factor] = score
    
    # Calculate overall feasibility
    overall_score = sum(feasibility_scores.values()) / len(feasibility_scores)
    
    # Determine top strengths and challenges
    sorted_factors = sorted(feasibility_scores.items(), key=lambda x: x[1], reverse=True)
    strengths = [factor for factor, score in sorted_factors[:3]]
    challenges = [factor for factor, score in sorted_factors[-3:]]
    
    return {
        "overall_score": round(overall_score, 2),
        "strengths": strengths,
        "challenges": challenges,
        "detailed_scores": feasibility_scores
    }

def evaluate_startup_idea(idea_text):
    """Main function to evaluate a startup idea."""
    # Categorize the idea
    category = categorize_idea(idea_text)
    
    # Evaluate feasibility
    feasibility = evaluate_feasibility(idea_text)
    
    # Analyze sentiment
    sentiment = analyze_sentiment(idea_text, category)
    
    # Get historical data
    historical_data = get_historical_data(category)
    
    return {
        "category": category,
        "feasibility": feasibility,
        "sentiment": sentiment,
        "historical_data": historical_data
    }

def generate_response(evaluation_result):
    """Generate a human-readable response from the evaluation results."""
    category = evaluation_result["category"]
    feasibility = evaluation_result["feasibility"]
    sentiment = evaluation_result["sentiment"]
    historical_data = evaluation_result["historical_data"]
    
    response = f"""
Based on my analysis, your startup idea falls into the *{category.capitalize()}* category.

**Feasibility Analysis:**
Overall Score: {feasibility['overall_score'] * 100:.0f}%

Key Strengths:
- {', '.join(feasibility['strengths'])}

Key Challenges:
- {', '.join(feasibility['challenges'])}

**Social Media Sentiment Analysis:**
The sentiment around similar ideas is generally {sentiment['overall']}.
- Positive aspects often mentioned: {', '.join(sentiment['positive_aspects'])}
- Concerns typically raised: {', '.join(sentiment['negative_aspects'])}

**Historical Success Rate:**
Similar startups in this category have a success rate of approximately {historical_data['success_rate'] * 100:.0f}%.
Average Initial Funding: {historical_data['avg_funding']}
Time to Profitability: {historical_data['avg_time_to_profitability']}

Common challenges for {category} startups include:
- {', '.join(historical_data['common_challenges'])}

Would you like more details on any specific aspect of this evaluation?
"""
    
    return response