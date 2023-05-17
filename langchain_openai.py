import os
import openai

from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()  # 读取 .env 文件
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)
text = "你是谁？"
print(llm(text))

