from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Define the Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short poem about {topic}."
)

# Initialize the Language Model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Create the Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the Chain
result = chain.invoke({"topic": "the ocean"})
print(result["text"])