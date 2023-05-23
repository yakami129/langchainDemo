# Import things that are needed generically
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from dotenv import load_dotenv
from pydantic import BaseModel, Field

## 初始化操作
load_dotenv()  # 读取 .env 文件

llm = ChatOpenAI(temperature=0)

## 自定义SerpAPI搜索工具
search = SerpAPIWrapper()
tools = [
    Tool.from_function(
        func=search.run,
        name="Search",
        description="useful for when you need to answer questions about current events"
    )
]

class CalculatorInput(BaseModel):
    question: str = Field()

## 自定义计算工具
llm_math_chain = LLMMathChain(llm=llm,verbose=True)
colculator_tool = Tool.from_function(
    func=llm_math_chain.run,
    name="colculator",
    description="useful for when you need to answer questions about math",
    args_schema=CalculatorInput
)
tools.append(colculator_tool)

## 初始化Agent
agent = initialize_agent(tools=tools,llm=llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

## 运行Agent
agent.run("今天上海的天气怎么样？它的华氏摄氏度是多少？用中文回复我答案")