from typing import Annotated, Any, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from chains import generate_chain, reflect_chain

REFLECT = "reflect"
GENERATE = "generate"


class MessageGraph(TypedDict):
    """_summary_

    Args:
        TypedDict (_type_): _description_
    """

    messages: Annotated[list[BaseMessage], add_messages]


def generation_node(state: MessageGraph) -> dict[str, list[BaseMessage]]:
    """_summary_

    Args:
        state (MessageGraph): _description_

    Returns:
        _type_: _description_
    """
    return {"messages": [generate_chain.invoke({"messages": state["messages"]})]}


def reflection_node(state: MessageGraph) -> dict[str, list[BaseMessage]]:
    result = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages": [HumanMessage(content=result.content)]}


def should_continue(state: MessageGraph) -> str:
    """_summary_

    Args:
        state (MessageGraph): _description_

    Returns:
        str: _description_
    """
    return END if len(state["messages"]) > 6 else REFLECT


builder: StateGraph[MessageGraph] = StateGraph(state_schema=MessageGraph)
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)
builder.add_conditional_edges(
    GENERATE, should_continue, path_map={REFLECT: REFLECT, END: END}
)
builder.add_edge(REFLECT, GENERATE)

graph = builder.compile()
print(graph.get_graph().draw_mermaid())


def main() -> None:
    print("Hello from Reflection Agent!")
    inputs: MessageGraph = {
        "messages": [
            HumanMessage(
                content="""Make this tweet better:"
                                @LangChainAI
        - newly Tool Calling feature is seriously underrated.

        After a long wait, it's  here- making the implementation of agents across different models with function calling - super easy.

        Made a video covering their newest blog post

                                """
            )
        ]
    }

    response = graph.invoke(inputs)
    print(response)


if __name__ == "__main__":
    main()
