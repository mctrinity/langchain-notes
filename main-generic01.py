from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import argparse
import re

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("--task", required=True, help="Task to generate content for")
parser.add_argument("--language", required=True, help="Language for the generated content")
args = parser.parse_args()

# Ensure the API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Define the Prompt Template to handle any type of content generation
prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="Write a well-structured {language} piece based on the topic '{task}'. "
             "Ensure the response is properly formatted, concise, and directly relevant to the topic. "
             "Do not include explanations, comments, or unnecessary text."
)

# Initialize the Language Model with increased token limit
llm = OpenAI(api_key=OPENAI_API_KEY, max_tokens=1500)

# ✅ Replace LLMChain with RunnableSequence
chain = prompt | llm  

# Run the Chain
result = chain.invoke({"language": args.language, "task": args.task})

# Extract the title from the first line of the result
lines = result.strip().split("\n")
title = lines[0] if lines else args.task

# ✅ Extract important keywords for a concise filename
keywords = re.findall(r"\b[A-Z][a-z]+\b", title)[:4]  # Capture up to 4 significant capitalized words
filename = "_".join(keywords) if keywords else "Generated_Content"
filename = filename[:50] + ".txt"  # Ensure filename is not too long

# ✅ Print only the clean result with a refined title
print(f"\n# {title}\n\n" + "\n".join(lines[1:]))

# ✅ Save output to a dynamically named file
with open(filename, "w", encoding="utf-8") as file:
    file.write(f"# {title}\n\n" + "\n".join(lines[1:]))
print(f"\n✅ Content saved to {filename}")

