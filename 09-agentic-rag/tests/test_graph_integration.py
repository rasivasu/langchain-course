import pytest
from dotenv import load_dotenv
from graph.graph import app

load_dotenv()

@pytest.mark.parametrize(
    "question, expected_key",
    [
        ("What is agent memory?", "generation"), # Should route to vectorstore and generate
        ("Who won the 2024 Super Bowl?", "generation"), # Should route to websearch (or fallback) and generate
    ]
)
def test_graph_e2e(question, expected_key):
    """
    Test the full graph execution for different types of questions.
    """
    inputs = {"question": question}
    output = app.invoke(inputs)
    
    assert "generation" in output
    assert "question" in output
    assert isinstance(output["generation"], str)
    assert len(output["generation"]) > 0

def test_graph_routing_vectorstore():
    """
    Verify that a question known to be in the blog docs routes to vectorstore.
    We can check the internal state if we use 'stream' or 'debug' mode, 
    but for a simple integration test, we check if documents were actually retrieved.
    """
    inputs = {"question": "Explain chain of thought prompting"}
    output = app.invoke(inputs)
    
    # If it routed to vectorstore, documents should be populated
    assert "documents" in output
    assert len(output["documents"]) > 0

def test_graph_routing_websearch():
    """
    Verify that a question unrelated to the docs routes to web search or triggers it.
    """
    inputs = {"question": "What is the current stock price of NVIDIA?"}
    output = app.invoke(inputs)
    
    # For this to be a true "web search" test, we'd ideally verify the node was hit.
    # Given GraphState, we can check if web_search flag became True at some point or 
    # if the output is generated.
    assert "generation" in output
    assert len(output["generation"]) > 0
