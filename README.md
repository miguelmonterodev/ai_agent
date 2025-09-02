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