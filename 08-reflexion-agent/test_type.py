from typing import Literal
from langgraph.graph import END

def foo() -> Literal["a", END]:
    return END

print(foo())
