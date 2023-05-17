
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import openai

## 初始化操作
load_dotenv()  # 读取 .env 文件
openai.api_key = os.getenv("OPENAI_API_KEY")

## 初始化OpenAI和Prompt的模版
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?")

## 创建一个简单的langchain链
chain = LLMChain(llm=llm,prompt=prompt)

## 执行langchain链
str =  chain.run("制造汽车");
print(str)

