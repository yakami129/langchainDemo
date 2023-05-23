import requests
from typing import Optional, Type
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

## 初始化操作
load_dotenv()  # 读取 .env 文件

search = SerpAPIWrapper()
llm = ChatOpenAI(temperature=0)
llm_math_chain = LLMMathChain(llm=llm,verbose=True)

        
@tool("post_message",return_direct=True)
def post_message(url: str, body: dict, parameters: Optional[dict] = None) -> str:
    """发送一个POST请求，并指定url和body、parameters"""
    result = requests.post(url, json=body, params=parameters)
    return f"Status: {result.status_code} - {result.text}"

@tool("get_message",return_direct=True)
def get_message(url: str, parameters: Optional[dict] = None) -> str:
    """发送一个GET请求，并指定url和parameters"""
    result = requests.get(url, params=parameters)
    return f"Status: {result.status_code} - {result.text}"

@tool("create_flow",return_direct=True)
def create_flow(create_flow_json: str) -> str:
    """创建一个工作流"""
    return f"create_flow_json:{create_flow_json}"

tools = [post_message,get_message,]
agent = initialize_agent(tools=tools,llm=llm,agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
agent.run("请通过http的方式请求www.baidu.com,body为{'z':'b'}")