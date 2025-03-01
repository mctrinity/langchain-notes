from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Define the Prompt Template
prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="Write a {language} text that follows the rules of a haiku. The haiku should be about {task}."
)


# Initialize the Language Model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Create the Chain using RunnableSequence
haiku_chain = prompt | llm  # Replaces LLMChain

# Run the Chain using .invoke()
result = haiku_chain.invoke({"language": "Python", "task": "the beauty of autumn"})
print(result)