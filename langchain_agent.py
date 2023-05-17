
import os
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import openai

## 初始化操作
load_dotenv()  # 读取 .env 文件


## 初始化语言模型
llm = OpenAI(temperature=0)

## 加载工具
tools = load_tools(["serpapi","llm-math"],llm=llm)

## 初始化代理
agent = initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

## 执行agent
agent.run("今天长沙的天气怎么样？它的华氏摄氏度是多少？")