# In this module we are adding checkpoints to store the references of previous context using mongodb
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

# llm initialization
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",   
    temperature=0.7
)


# class state is the initial state we pass before invoking the graph
class State(TypedDict):
    messages: Annotated[list,add_messages]

def chatbot(state:State):
    print("\nInside chatbot node", state)

    # calling llm
    response = llm.invoke(state["messages"])
    return {"messages":[response]}



# graph_building
graph_builder = StateGraph(State)

# adding nodes
graph_builder.add_node("chatbot",chatbot)

# adding edges to determine flow
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)

# compile with the checkpoint
def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

DB_URI = "mongodb://localhost:27017"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {
        "configurable" : {
            "thread_id" : "name"
        }
    }

    for chunk in graph_with_checkpointer.stream({"messages":["what is my name"]},config,stream_mode="values"):
        chunk["messages"][-1].pretty_print()



