from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langsmith import Client

llm = ChatOpenAI(temperature=0)
client = Client()

# Pull a standard RAG prompt from the LangChain Hub
# This prompt typically includes placeholders for {context} and {question}
prompt = client.pull_prompt("rlm/rag-prompt", dangerously_pull_public_prompt=True)

# The generation_chain synthesizes the final answer using the retrieved context
generation_chain = prompt | llm | StrOutputParser()
