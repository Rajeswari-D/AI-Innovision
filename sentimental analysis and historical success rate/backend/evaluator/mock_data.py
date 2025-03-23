# Mock social media sentiment data
SOCIAL_MEDIA_SENTIMENT = {
    "tech": {
        "positive": ["innovative", "disruptive", "revolutionary", "efficient", "scalable"],
        "negative": ["overdone", "expensive", "complicated", "risky", "saturated"]
    },
    "food": {
        "positive": ["delicious", "convenient", "healthy", "sustainable", "affordable"],
        "negative": ["competitive", "low-margin", "perishable", "regulated", "capital-intensive"]
    },
    "health": {
        "positive": ["necessary", "impactful", "growing", "profitable", "regulated"],
        "negative": ["complex", "regulated", "expensive", "slow-growth", "high-barrier"]
    },
    "education": {
        "positive": ["meaningful", "scalable", "needed", "impactful", "digital"],
        "negative": ["slow-adoption", "underfunded", "complex", "regulated", "competitive"]
    },
    "finance": {
        "positive": ["lucrative", "growing", "digital", "necessary", "scalable"],
        "negative": ["regulated", "competitive", "trust-dependent", "complex", "high-security"]
    },
    "ecommerce": {
        "positive": ["convenient", "scalable", "global", "growing", "low-overhead"],
        "negative": ["competitive", "logistics-heavy", "low-margin", "customer-acquisition", "return-rates"]
    }
}

# Mock historical startup success rates
HISTORICAL_SUCCESS_RATES = {
    "tech": {
        "success_rate": 0.15,
        "avg_funding": "$2.5M",
        "avg_time_to_profitability": "3-5 years",
        "common_challenges": ["technical feasibility", "market adoption", "scaling issues"]
    },
    "food": {
        "success_rate": 0.12,
        "avg_funding": "$1.2M",
        "avg_time_to_profitability": "2-3 years",
        "common_challenges": ["food safety regulations", "supply chain complexity", "high overhead"]
    },
    "health": {
        "success_rate": 0.08,
        "avg_funding": "$3.5M",
        "avg_time_to_profitability": "5-7 years",
        "common_challenges": ["regulatory approvals", "insurance relationships", "lengthy sales cycles"]
    },
    "education": {
        "success_rate": 0.10,
        "avg_funding": "$1.0M",
        "avg_time_to_profitability": "3-4 years",
        "common_challenges": ["slow institutional adoption", "funding constraints", "proof of outcomes"]
    },
    "finance": {
        "success_rate": 0.07,
        "avg_funding": "$4.0M",
        "avg_time_to_profitability": "4-6 years",
        "common_challenges": ["regulatory compliance", "security concerns", "trust building"]
    },
    "ecommerce": {
        "success_rate": 0.20,
        "avg_funding": "$1.8M",
        "avg_time_to_profitability": "2-4 years",
        "common_challenges": ["customer acquisition costs", "logistics", "inventory management"]
    }
}

# Generic response templates for any category not in our mock data
DEFAULT_SENTIMENT = {
    "positive": ["innovative", "promising", "potential", "interesting", "timely"],
    "negative": ["competitive", "challenging", "unproven", "complex", "resource-intensive"]
}

DEFAULT_SUCCESS_RATE = {
    "success_rate": 0.10,
    "avg_funding": "$2.0M",
    "avg_time_to_profitability": "3-5 years",
    "common_challenges": ["market validation", "funding", "team building", "execution"]
}

# Feasibility factors
FEASIBILITY_FACTORS = [
    "market size", 
    "competition", 
    "regulatory environment", 
    "technical complexity", 
    "capital requirements",
    "time to market",
    "scalability potential",
    "team requirements"
]