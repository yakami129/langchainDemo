
from dotenv import load_dotenv
from langchain import OpenAI, ConversationChain

## 初始化操作
load_dotenv()  # 读取 .env 文件

## 初始化简单类型的内存
llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm,verbose=True)

## 开始聊天
outputA = conversation.predict(input="湖南有多少城市？")
print(outputA)

outputB = conversation.predict(input="它有哪些好玩的旅游景点？")
print(outputB)

