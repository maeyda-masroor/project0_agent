import os
from dotenv import load_dotenv
from agents import Agent, Runner

# Load environment variables from .env file
load_dotenv()

# Access your API key
api_key = os.getenv("TOKEN")
if not api_key:
   raise ValueError("OPENAI_API_KEY not found in .env file")