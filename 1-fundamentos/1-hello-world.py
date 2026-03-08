from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.5
)

response = llm.invoke("Say hello to the world in one sentence")

print(response.content)