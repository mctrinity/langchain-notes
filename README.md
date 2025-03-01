# 🌟 LangChain Haiku Generator

Welcome to the **LangChain Haiku Generator**, a Python project that uses **LangChain** and **OpenAI's LLM** to generate beautifully structured haikus based on a given topic.

## 🔧 Features
- ✨ Generates **AI-powered haikus** using natural language input
- ✨ Supports **different topics** for dynamic haiku creation
- ✨ Allows **multiple languages**, including English, Japanese, and more
- ✨ Uses **LangChain's RunnableSequence** for structured AI output
- ✨ ✅ Clean output with no unnecessary print statements

## 📚 Requirements
To run this project, make sure you have the following dependencies installed:
```sh
pip install langchain langchain_openai python-dotenv
```
Also, create a `.env` file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🛠️ Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/langchain-haiku-generator.git
   cd langchain-haiku-generator
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the script:**
   ```sh
   python haiku.py
   ```

## 🎨 Usage
### **Generating a Haiku**
Simply run the script to generate a haiku about a default topic:
```sh
python haiku.py
```

### **Generating a Haiku About a Specific Topic**
Modify the `task` parameter in the script:
```python
result = haiku_chain.invoke({"language": "English", "task": "cherry blossoms in spring"})
print(result.strip())
```

### **Generating Multiple Haikus at Once**
Loop through different topics:
```python
topics = ["autumn leaves", "the ocean", "mountains", "the sound of rain"]
for topic in topics:
    result = haiku_chain.invoke({"language": "English", "task": topic})
    print(result.strip(), "\n")
```

## 🌍 Multi-Language Support
You can generate haikus in different languages:
```python
result = haiku_chain.invoke({"language": "Japanese", "task": "cherry blossoms"})
print(result.strip())
```
Example output in Japanese:
```
桜咲く  
風に舞い散る  
春の夢  
```

## 🏆 Future Enhancements
- ✨ **Improve prompt engineering** for more structured haikus
- ✨ **Add syllable validation** to ensure strict 5-7-5 format
- ✨ **Build a web-based UI** using Flask or Streamlit
- ✨ **Create a Discord bot** that generates haikus on demand

## ✨ Contributing
Feel free to **fork** this project, submit **issues**, and create **pull requests** to improve the Haiku Generator!

## 💪 Credits
Developed using **LangChain**, **OpenAI**, and **Python**.

Happy haiku writing! 🌟

