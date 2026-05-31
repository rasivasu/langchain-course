# from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_core.messages import AIMessage
from langgraph.graph import END, MessagesState, StateGraph

from nodes import run_agent_reasoning, tool_node

AGENT_REASON = "agent_reason"
ACT = "act"
LAST_MESSAGE_INDEX = -1


def should_continue(state: MessagesState) -> str:
    last_message = state["messages"][LAST_MESSAGE_INDEX]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return ACT
    return END


flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)

flow.add_node(ACT, tool_node)
flow.add_conditional_edges(AGENT_REASON, should_continue, {END: END, ACT: ACT})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()  # app.get_graph().draw_mermaid_png(output_file_path="flow.png")


def main():
    print("Hello ReAct LangGraph with Function Calling!")
    res = app.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What is the temperature in Tokyo? List it and then triple it"
                )
            ]
        }
    )
    print(res["messages"][LAST_MESSAGE_INDEX].content)


if __name__ == "__main__":
    main()
