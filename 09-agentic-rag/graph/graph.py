from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from graph.chains.answer_grader import answer_grader
from graph.chains.hallucination_grader import GradeHallucinations, hallucination_grader
from graph.consts import GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEB_SEARCH
from graph.nodes import generate, grade_documents, retrieve, web_search
from graph.state import GraphState


def should_generate_or_search_web(state: GraphState) -> str:
    """
    Determines whether to generate an answer or add web search based on the hallucination score.

    Args:
        state (GraphState): The current state of the graph.

    Returns:
        str: The next node to execute ("GENERATE" or "WEB_SEARCH").
    """
    print("---ASSESS GRADED DOCUMENTS---")

    # grade_documents function reviews all the documents retrieved from the vector store
    # and grades them based on their relevance to the question. If any document is not relevant,
    # web search is triggered to find more up-to-date information.

    # The StateGraph calls grade_documents function to determine whether to generate an answer
    # or add web search. And it adds the web_search flag to the state to indicate whether
    # web search should be triggered.

    if state["web_search"]:
        print(
            "---DECISION: NOT ALL DOCUMENTS ARE RELEVANT TO QUESTION, INCLUDE WEB SEARCH---"
        )
        return WEB_SEARCH
    else:
        print("---DECISION: ALL DOCUMENTS ARE RELEVANT TO QUESTION, GENERATE---")
        return GENERATE


def grade_generation_grounded_in_documents_and_questions(state: GraphState) -> str:
    """
    This function grades the 'generation' based on whether it is grounded in the documents and
    addresses the question. It uses the hallucination_grader to check if the generation is
    grounded in the documents, and the answer_grader to check if it addresses the question.
    """

    print("---CHECK HALLUCINATIONS---")
    question = state["question"]  # The question is passed by main.py to the graph
    generation = state["generation"]  # Created by the generation node
    documents = state["documents"]  # Created by the retrieve node

    score: GradeHallucinations = hallucination_grader.invoke(  # pyright: ignore[reportAssignmentType]
        {"documents": documents, "generation": generation}
    )

    if score.binary_score:
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        print("---GRADE GENERATION vs QUESTIONS---")
        score = answer_grader.invoke({"question": question, "generation": generation})
        if score.binary_score:
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS---")
        return "not supported"


workflow = StateGraph(GraphState)
workflow.add_node(
    RETRIEVE, retrieve
)  # Retrieves documents from the vector store based on the question
workflow.add_node(
    GRADE_DOCUMENTS, grade_documents
)  # Grades the retrieved documents against the question
workflow.add_node(
    GENERATE, generate
)  # Generates an answer using LLM, based on the question and retrieved documents
workflow.add_node(
    WEB_SEARCH, web_search
)  # Performs a web search using TavilySearch, if the generation is not grounded in the documents

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    should_generate_or_search_web,
    [GENERATE, WEB_SEARCH],
)
workflow.add_conditional_edges(
    GENERATE,
    grade_generation_grounded_in_documents_and_questions,
    {"not supported": GENERATE, "useful": END, "not useful": WEB_SEARCH},
)
workflow.add_edge(WEB_SEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")
