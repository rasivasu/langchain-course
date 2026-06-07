from pprint import pprint

from dotenv import load_dotenv

from graph.chains.generation import generation_chain
from graph.chains.hallucination_grader import GradeHallucinations, hallucination_grader
from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from graph.chains.router import RouteQuery, question_router
from ingestion import retriever

load_dotenv()


def test_retrival_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(  # pyright: ignore[reportAssignmentType]
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "yes"


def test_retrival_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(  # pyright: ignore[reportAssignmentType]
        {"question": "how to make pizaa", "document": doc_txt}
    )

    assert res.binary_score == "no"


def test_generation_chain() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    generation = generation_chain.invoke({"question": question, "context": docs})
    pprint(generation)


def test_hallucinator_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)

    generation = generation_chain.invoke({"question": question, "context": docs})
    res: GradeHallucinations = hallucination_grader.invoke(  # pyright: ignore[reportAssignmentType]
        {"documents": docs, "generation": generation}
    )
    assert res.binary_score


def test_hallucinator_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)

    res: GradeHallucinations = hallucination_grader.invoke(  # pyright: ignore[reportAssignmentType]
        {
            "documents": docs,
            "generation": "In order to make pizza, we need to start with the dough",
        }
    )
    assert not res.binary_score


def test_route_to_vectorstore() -> None:
    question = "agent memory"

    res: RouteQuery = question_router.invoke({"question": question})  # pyright: ignore[reportAssignmentType]
    assert res.datasource == "vectorstore"


def test_route_to_websearch() -> None:
    question = "How to make Pizza?"

    res: RouteQuery = question_router.invoke({"question": question})  # pyright: ignore[reportAssignmentType]
    assert res.datasource == "websearch"
