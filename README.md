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
You can think of tokens as the currency of LLMs. They are the way that LLMs measure how much text they have to process. Tokens are roughly 4 characters for most models. It's important when working with LLM APIs to understand how many tokens you're using.
We'll be staying well within the free tier limits of the Gemini API, but we'll still monitor our token usage!
## Prerequisites
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
