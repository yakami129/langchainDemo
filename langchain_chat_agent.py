from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from dotenv import load_dotenv

## 初始化操作
load_dotenv()  # 读取 .env 文件

## 初始化聊天AI模型
chat = ChatOpenAI(temperature=0)

## 初始化llm模型和工具
llm = OpenAI(temperature=0)
tools = load_tools(["serpapi","llm-math"],llm=llm)

## 初始化Agent
agent = initialize_agent(tools,chat,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

## 执行Agent
agent.run("目前大语言模型的发展情况如何？哪家公司做得好？用中文回复")
