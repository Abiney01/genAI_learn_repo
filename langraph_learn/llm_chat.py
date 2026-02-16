# we are using langgraph to structure the code flow easily thorugh nodes and edges.
# this makes to better to understand the program execution
# this time instead of static message we are making use of llm

from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

# llm initialization
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",   
    temperature=0.7
)


# class state is the initial state we pass before invoking the graph
class State(TypedDict):
    messages: Annotated[list,add_messages]

# sample nodes which will be appended to add_messages 
def chatbot(state:State):
    print("\nInside chatbot node", state)

    # calling llm
    response = llm.invoke(state["messages"])
    return {"messages":[response]}

def sampleNode(state:State):
    print("\nInside sampleNode", state)
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
updated_state = graph.invoke({"messages":["heyy,there!"]})

# flow of execution -> START -> chatbot -> sampleNode -> END
print("\nupdated_state",updated_state)
