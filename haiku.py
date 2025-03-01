from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
import os
import re

# Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

# ✅ Define the Haiku Prompt
prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="Write a {language} function that generates a haiku about {task}. "
             "The function should return the haiku as a string and should not print anything."
)

# ✅ Initialize the Language Model
llm = OpenAI(api_key=OPENAI_API_KEY)

# ✅ Use RunnableSequence
haiku_chain = RunnableSequence(prompt, llm)

# ✅ Run the Chain Using `.invoke()`
generated_code = haiku_chain.invoke({"language": "English", "task": "a quiet snowfall"})

# ✅ Remove any print statements from the generated code
cleaned_code = re.sub(r"print\(.+\)", "", generated_code)

# ✅ Extract the function name dynamically
match = re.search(r"def (\w+)\(", cleaned_code)
if match:
    function_name = match.group(1)  # Extract function name
else:
    exit()  # Exit quietly if function name is not found

# ✅ Execute the cleaned function safely
try:
    exec(cleaned_code)  # Defines the function in Python
    result = eval(f"{function_name}()")  # Dynamically call the function
    print(result.strip())  # ✅ Only print the haiku, no extra text
except Exception:
    exit()  # Quietly exit if execution fails
