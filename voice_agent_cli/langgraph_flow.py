import speech_to_text as STT
from langgraph.graph import StateGraph
from typing import TypedDict
class State(dict):
    text : str
    intent : str

def input_node(state):
    print("Input Received",state.get("text","No text found"))
    return state

def parser_node(state):
    text = state["text"]
    if "create" in text:
        intent = "create_file"
    elif "run" in text:
        intent = "run_code"
    else:
        intent = "unknown"

    state["intent"] = intent
    print("Parsed intent",intent)
    return state

def router_node(state):
    intent = state["intent"]
    if intent == "create_file":
        print("📁 Action: Creating file...")
    elif intent == "run_code":
        print("⚙️ Action: Running code...")
    else:
        print("❓ Unknown command")

    return state

def build_graph():
    graph = StateGraph(State)
    graph.add_node("input",input_node)
    graph.add_node("parser",parser_node)
    graph.add_node("router",router_node)

    graph.set_entry_point("input")
    graph.add_edge('input','parser')
    graph.add_edge('parser','router')

    return graph.compile()
