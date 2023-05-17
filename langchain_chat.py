from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

## 初始化操作
load_dotenv()  # 读取 .env 文件

chat = ChatOpenAI(temperature=0)
messages = [
    SystemMessage(content="你是现在是灌篮高手中樱木花道，说话的语气需要强硬，请保持当前的角色扮演"),
    HumanMessage(content="你觉得流川枫的球技怎么样，比得过蔡徐坤吗？")
]
response = chat(messages=messages)
print(response)