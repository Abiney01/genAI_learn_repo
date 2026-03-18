import speech_to_text as STT
from langgraph.graph import StateGraph
from typing import TypedDict, Dict, Any
from langgraph.checkpoint.mongodb import MongoDBSaver
from llm_client import generate_command
from executor import execute_command

class State(TypedDict):
    text : str
    llm_output: Dict[str, Any]

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
    user_text = state["text"]
    result = generate_command(user_text)
    print("\n🤖 Gemini Structured Output:\n", result)
    try:
        command = result["arguments"]["command"]
    except:
        print("❌ Invalid LLM response")
        return state
    execute_command(command)

    state["command"] = command
    return state

def build_graph(checkpointer=None):
    graph = StateGraph(State)
    graph.add_node("input",input_node)
    graph.add_node("parser",parser_node)
    graph.add_node("router",router_node)

    graph.set_entry_point("input")
    graph.add_edge('input','parser')
    graph.add_edge('parser','router')

    return graph.compile(checkpointer=checkpointer)
