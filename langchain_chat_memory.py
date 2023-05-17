from dotenv import load_dotenv
from langchain.prompts import(
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

## 初始化操作
load_dotenv()  # 读取 .env 文件

## 初始化聊天模版
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        template="你现在扮演的是一名产品专家，如果用户和你提出了，非产品相关的问题，你需要拒绝回答，如果用户和你提出了产品相关的问题，你需要一步一步解答"
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

 ## 初始化聊天模型、添加聊天记忆
llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory,prompt=prompt,llm=llm)

outputA = conversation.predict(input="你好")
print(outputA)

outputB = conversation.predict(input="现在美国总统是谁？")
print(outputB)

outputC = conversation.predict(input="AI产品的发展前景怎么样？")
print(outputC)