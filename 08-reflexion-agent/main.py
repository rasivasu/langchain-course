from typing import Any, Literal

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.graph.state import CompiledStateGraph

from chains import first_responder, revisor
from tool_executor import execute_tools

MAX_ITERATIONS = 2


def draft_node(state: MessagesState) -> dict[str, list[AIMessage]]:
    """Draft the initial response."""
    response = first_responder.invoke({"messages": state["messages"]})
    return {"messages": [response]}


def revise_node(state: MessagesState) -> dict[str, list[AIMessage]]:
    """Revise the answer based on tool results."""
    response = revisor.invoke({"messages": state["messages"]})
    return {"messages": [response]}


def should_continue(state: MessagesState) -> Literal["execute_tools"] | str:
    """Determine whether to continue or end based on iteration count."""
    count_tool_visits = sum(
        isinstance(message, ToolMessage) for message in state["messages"]
    )
    if count_tool_visits > MAX_ITERATIONS:
        return END
    return "execute_tools"


builder: StateGraph[MessagesState, None, MessagesState, MessagesState] = StateGraph(
    MessagesState
)
builder.add_node("draft", draft_node)
builder.add_node("execute_tools", execute_tools)
builder.add_node("revise", revise_node)
builder.add_edge(START, "draft")
builder.add_edge("draft", "execute_tools")
builder.add_edge("execute_tools", "revise")
builder.add_conditional_edges("revise", should_continue, ["execute_tools", END])
graph: CompiledStateGraph[MessagesState, None, MessagesState, MessagesState] = (
    builder.compile()
)

print(graph.get_graph().draw_mermaid())


res: dict[str, Any] | Any = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Write about AI-Powered SOC / autonomous soc problem domain, list startups that do that and raised capital."
            )
        ]
    }
)
# Extract the final answer from the last message with tool calls
last_message = res["messages"][-1]
if isinstance(last_message, AIMessage) and last_message.tool_calls:
    print(last_message.tool_calls[0]["args"]["answer"])
print(res)
