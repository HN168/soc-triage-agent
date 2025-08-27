"""Configuration settings for SOC Triage Agent"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# AWS Configuration
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION', 'us-west-2')

# Agent Settings
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
DEMO_MODE = os.getenv('DEMO_MODE', 'false').lower() == 'true'
MAX_FINDINGS_PER_RUN = int(os.getenv('MAX_FINDINGS_PER_RUN', '10'))

def validate_required_settings():
    """Check that required settings are present."""
    missing = []
    
    if not VIRUSTOTAL_API_KEY and not DEMO_MODE:
        missing.append('VIRUSTOTAL_API_KEY')
    
    if not OPENAI_API_KEY and not DEMO_MODE:
        missing.append('OPENAI_API_KEY')
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    return True