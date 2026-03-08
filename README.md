# ai-systems-langchain

Hands-on exploration of **LangChain** for building production-grade **LLM systems, agents, and retrieval pipelines using Python**.

This repository contains practical examples from the **AI Systems MBA course**, focusing on how to build modern AI applications using LangChain, OpenAI models, and Python.

The goal is to learn by doing, starting with simple examples and gradually moving toward more advanced AI systems such as agents, tools, and retrieval-based applications.

---

# Repository Structure

Examples are organized by topic and learning stage.


ai-systems-langchain
│
├─ 1-fundamentos/
│ ├─ 1-hello-world.py
│
├─ .env.example
├─ .gitignore
└─ README.md


Each folder represents a learning module from the course.

---

# Requirements

You need the following installed:

- Python **3.10+**
- pip
- Git

Recommended tools:

- VS Code
- Python extension for VS Code

Check your Python version:


python3 --version


---

# Environment Setup

Create a Python virtual environment.


python3 -m venv .venv


Activate the virtual environment.

### Linux / Mac


source .venv/bin/activate


### Windows


.venv\Scripts\activate


After activation you should see:


(.venv)


in your terminal prompt.

---

# Install Dependencies

Install the required libraries:


pip install langchain langchain-openai python-dotenv


Optional (recommended for development):


pip install ipykernel


Verify installation:


pip list


You should see packages like:


langchain
langchain-core
langchain-openai
python-dotenv


---

# OpenAI API Key

Create a `.env` file in the project root.


touch .env


Add your OpenAI API key:


OPENAI_API_KEY=your_api_key_here


Example `.env` file:


OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx


Do **not** commit this file to GitHub.

---

# Running an Example

Run the first example:


python 1-fundamentos/1-hello-world.py


Expected output:


Hello, world!



---

# Example Code

Example LangChain usage:

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0
)

response = model.invoke("Hello world")

print(response.content)


Common Issues
Missing API Key

Error:
OpenAIError: The api_key client option must be set
Fix:
Make sure .env exists and contains:
OPENAI_API_KEY=your_key


LangSmith Errors

If you see errors related to LangSmith:
Failed to POST https://api.smith.langchain.com
Disable tracing:
export LANGCHAIN_TRACING_V2=false


Recommended Workflow

Always start your session with:
source .venv/bin/activate
Then run examples.


Learning Path

The repository will evolve following the course progression:
LangChain basics
Chat models
Prompt templates
Chains
Tools
Agents
Retrieval (RAG)
Production-ready AI systems


License

MIT License