# we are using langgraph to structure the code flow easily thorugh nodes and edges.
# this makes to better to understand the program execution

from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START,END

# class state is the initial state we pass before invoking the graph
class State(TypedDict):
    messages: Annotated[list,add_messages]

# sample nodes which will be appended to add_messages 
def chatbot(state:State):
    print("\n")
    print("Inside chatbot node", state)
    return {"messages":["Hi,This is a message from chatbot node"]}

def sampleNode(state:State):
    print("\n")
    print("Inside sampleNode", state)
    return {"messages":["Sample node message appended"]}

# graph_building
graph_builder = StateGraph(State)

# adding nodes
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("sampleNode",sampleNode)

# adding edges to determine flow
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot","sampleNode")
graph_builder.add_edge("sampleNode",END)

# compilation of graph
graph = graph_builder.compile()

# initial state message for invoking the graph
updated_state = graph.invoke({"messages":["Hi,from outside world"]})

# flow of execution -> START -> chatbot -> sampleNode -> END
print("updated_state",updated_state)
