from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Define the Prompt Template
prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="Write a {language} function that {task}. The function should be well-structured and return the correct output."
)

# Initialize the Language Model
llm = OpenAI(api_key=OPENAI_API_KEY)

# Create the Chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the Chain
result = chain.invoke({"language": args.language, "task": args.task})
print(result["text"])