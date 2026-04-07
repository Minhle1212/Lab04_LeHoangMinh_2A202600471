import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="o4-mini")
print(llm.invoke("Hello?").content)



