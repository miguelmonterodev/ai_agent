# ai_agent
## Introduction
[Agentic AI](https://en.wikipedia.org/wiki/Agentic_AI) is a class of artificial intelligence that focuses on autonomous systems that can make decisions and perform tasks with or without human intervention. The independent systems automatically respond to conditions, with procedural, algorithmic, and human-like creative steps, to produce process results.
We are building an AI Agent using Google's free Gemini API.
## What does the Agent do?
The program we're building is a CLI tool that:
- Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽")
- Chooses from a set of predefined functions to work on the task, for example:
    - Scan the files in a directory
    - Read a file's contents
    - Overwrite a file's contents
    - Execute the python interpreter on a file
- Repeats step 2 until the task is complete (or it fails miserably, which is possible)
## Python Set up
Virtual environment:
```Bash
uv init your-project-name
cd your-project-name
uv venv
source .venv/bin/activate #Activate the virtual environment
```
Use uv to add two dependencies to the project. They will be added to the file pyproject.toml:
```Bash
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```
To run the project using the uv virtual environment, you use: ```uv run main.py```
## Gemini
Large Language Models (LLMs) are the AI technology that have been making all the waves in the AI world recently. Products like: ChatGPT, Claude, Cursor, Google Gemini... Are all powered by LLMs. For the purposes of this project, you can think of an LLM as a smart text generator. It works just like ChatGPT: you give it a prompt, and it gives you back some text that it believes answers your prompt. We're going to use [Google's Gemini API](https://ai.google.dev/gemini-api) to power our agent in this course. It's reasonably smart, but more importantly for us, it has a free tier.
### Tokens
You can think of tokens as the currency of LLMs. They are the way that LLMs **measure how much text they have to process**. Tokens are roughly 4 characters for most models. It's important when working with LLM APIs to understand how many tokens you're using.
We'll be staying well within the free tier limits of the Gemini API, but we'll still monitor our token usage!
## Prerequisites
- Python 3.10+ installed 
- uv project and package manager
- Access to a Unix-like shell (e.g. zsh or bash)
- An account on [Google AI Studio](https://aistudio.google.com/prompts/new_chat)
- ["Create API Key"](https://ai.google.dev/gemini-api/docs/api-key)
## Roles
The conversation has a history, and if we keep track of that history, then with each new prompt, the model can see the entire conversation and respond within the larger context of the conversation.
Importantly, each message in the conversation has a "role". In the context of a chat app your conversations would look like this:
- user: "What is the meaning of life?"
- model: "42"
- user: "Wait, what did you just say?"
- model: "42. It's is the answer to the ultimate question of life, the universe, and everything."
- user: "But why?"
- model: "Because Douglas Adams said so."
So, while our program will still be "one-shot" for now, let's update our code to store a list of messages in the conversation, and pass in the "role" appropriately.
## Functions
### Get directory content
- [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath): Get an absolute path from a relative path
- [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join): Join two paths together safely (handles slashes)
- [`.startswith()`](https://docs.python.org/3/library/stdtypes.html#str.startswith): Check if a string starts with a substring
- [`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir): Check if a path is a directory
- [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir): List the contents of a directory
- [`os.path.getsize()`](https://docs.python.org/3/library/os.path.html#os.path.getsize): Get the size of a file
- [`os.path.isfile()`](https://docs.python.org/3/library/os.path.html#os.path.isfile): Check if a path is a file
- [`.join()`](https://docs.python.org/3/library/stdtypes.html#str.join): Join a list of strings together with a separator
### Get file content
```python
MAX_CHARS = 10000

with open(file_path, "r") as f:
    file_content_string = f.read(MAX_CHARS)
```
### Write file
We'll give our agent the ability to write and overwrite files.
## ai-agent to run arbitary python code
Security risks:
- We'll only allow the LLM to run code in a specific directory (the working_directory).
- We'll use a 30-second timeout to prevent it from running indefinitely.
**This program does not have all the security and safety features that a production AI agent would have. Use it as a learning purpose.**
["subprocess.run"](https://docs.python.org/3/library/subprocess.html)
```python
subprocess.run(args=["python", file_path, arguments], cwd=abs_dir_path, timeout=30, capture_output=True)
```
