from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class RouteQuery(BaseModel):
    """
    Data model for the router's output.
    Routes a user query to either the local vectorstore or a general web search.
    """

    # Since the field contains elipses, the 'datasource' variable need to be assigned
    # a value when the RouteQuery object is instantiated
    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question, decide whether to route it to the vectorstore or websearch.",
    )


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# Use structured output to ensure the router returns a valid datasource literal
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
Use the vectorstore for questions on these topics. For all else, use web-search"""

route_prompt = ChatPromptTemplate.from_messages(
    [("system", system), ("human", "{question}")]
)

# The question_router chain decides the initial entry point of the graph
question_router = route_prompt | structured_llm_router
