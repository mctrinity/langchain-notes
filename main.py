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
parser.add_argument("--title", default=None, help="Optional custom title for the generated content")
parser.add_argument("--output-dir", default="output", help="Directory to save the generated content")
args = parser.parse_args()

# Ensure the API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# Define the Prompt Template to handle any type of content generation
prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="Write a vivid and immersive {language} story based on the topic '{task}'. "
             "Make it engaging with strong character development, dynamic action, and rich descriptions. "
             "Ensure the plot is exciting, filled with unexpected twists, and a satisfying resolution. "
             "Use a cinematic storytelling style with a mix of dialogue and action. "
             "Do not include explanations, comments, or unnecessary text."
)


# Initialize the Language Model with increased token limit
llm = OpenAI(api_key=OPENAI_API_KEY, max_tokens=1500)

# ✅ Replace LLMChain with RunnableSequence
chain = prompt | llm  

# Run the Chain
result = chain.invoke({"language": args.language, "task": args.task})

# Extract the lines from the result
lines = result.strip().split("\n")

# Extract the title from the first line of the result, or use the provided title
title = args.title if args.title else lines[0] if lines else args.task

# ✅ Extract key nouns for a concise filename
keywords = re.findall(r"\b[A-Z][a-z]+\b", title)[:4]  # Capture up to 4 significant words
filename = "_".join(keywords) if keywords else "Generated_Content"
filename = filename[:50] + ".txt"  # Ensure filename is not too long

# ✅ Create output directory if it doesn't exist
os.makedirs(args.output_dir, exist_ok=True)
file_path = os.path.join(args.output_dir, filename)

# ✅ Print only the clean result with a refined title
print(f"\n# {title}\n\n" + "\n".join(lines[1:]))

# ✅ Save output to a dynamically named file in the specified directory
with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"# {title}\n\n" + "\n".join(lines[1:]))
print(f"\n✅ Content saved to {file_path}")

