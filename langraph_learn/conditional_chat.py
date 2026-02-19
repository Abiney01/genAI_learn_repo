# we are using langgraph to structure the code flow easily thorugh nodes and edges.
# this makes to better to understand the program execution
# this time we are making use of conditional edges to route to different nodes

import os
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph import StateGraph, START,END
from typing import Optional,Literal
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# class state is the initial state we pass before invoking the graph
class State(TypedDict):
    user_query : str
    llm_output : Optional[str]
    is_good : Optional[str]

def chatbot(state:State):
    print("\nchatbot node", state)
    response = client.chat.completions.create(
        model= "gemini-3-flash-preview",
        messages=[
            {"role":"user","content":state.get("user_query")}
        ]
    ) 
    state['llm_output'] = response.choices[0].message.content
    return state

# Deciding Node
def evaluate_response(state:State)->Literal['chatbot2',"end_node"]:
    print("\nevaluate node", state)
    if False:
        return "end_node"
    return "chatbot2"

def chatbot2(state:State):
    print("chatbot2 node", state)
    response = client.chat.completions.create(
        model= "gemini-3-flash-preview",
        messages=[
            {"role":"user","content":state.get("user_query")}
        ]
    ) 
    state['llm_output'] = response.choices[0].message.content
    return state

def end_node(state:State):
    print("\nend node")
    return state

graph_buider = StateGraph(State)
graph_buider.add_node("chatbot",chatbot)
graph_buider.add_node("chatbot2",chatbot2)
graph_buider.add_node("end_node",end_node)

graph_buider.add_edge(START,"chatbot")
graph_buider.add_conditional_edges("chatbot",evaluate_response)
graph_buider.add_edge("chatbot2","end_node")
graph_buider.add_edge("end_node",END)

graph = graph_buider.compile()
updated_state = graph.invoke(State({"user_query":"hey what is 2+2?"}))
print(updated_state)
