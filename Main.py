# Main.py
# Simple CLI app using Langchain & Groq LLM
# Reads config from config.props, loops for user questions


import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Helper to load properties from a .props file
def load_props(filepath):
    props = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                props[k.strip()] = v.strip()
    return props

# Load config

config = load_props('config.props')
GROQ_API_KEY = config.get('GROQ_API_KEY')
# Use the new recommended model as default
GROQ_MODEL = config.get('GROQ_MODEL', 'openai/gpt-oss-20b')

if not GROQ_API_KEY:
    print("GROQ_API_KEY not set in config.props!")
    exit(1)

# Set API key as env var for langchain-groq
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

# Initialize Groq LLM
llm = ChatGroq(model=GROQ_MODEL)

print("Welcome to the Langchain-Groq CLI! Type 'exit' to quit.")
while True:
    question = input("\nYour question: ")
    if question.strip().lower() in ("exit", "quit"):
        print("Goodbye!")
        break
    # Send user question to LLM
    response = llm([HumanMessage(content=question)])
    print("LLM Response:", response.content)