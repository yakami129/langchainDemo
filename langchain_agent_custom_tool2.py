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

class CustomSearchTool(BaseTool):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events"
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        print("print-ai:",query)
        print("print-ai:",run_manager)
        return search.run(query)
    
    async def _arun(self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")
    
class CalculatorInput(BaseModel):
    question: str = Field()

class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "useful for when you need to answer questions about math"
    args_schema: Type[BaseModel] = CalculatorInput
    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool."""
        print("print-ai:",query)
        print("print-ai:",run_manager)
        return llm_math_chain.run(query)
    async def _arun(self, query: str,  run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Calculator does not support async")
    
tools = [CustomSearchTool(),CustomCalculatorTool()]
agent = initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

agent.run("今天上海的天气怎么样？它的华氏摄氏度是多少？用中文回复我答案")