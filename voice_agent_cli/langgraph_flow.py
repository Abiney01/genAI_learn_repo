from langgraph.graph import StateGraph
from typing import TypedDict, Dict, Any
from llm_client import generate_command
from executor import execute_plan


class State(TypedDict):
    text: str
    plan: Dict[str, Any]
    result: str
    error: str
    history : list


# 🟢 Input Node
def input_node(state):
    print("🎤 Input:", state.get("text"))
    return state


# 🧠 Planner Node (LLM)
def planner_node(state):
    user_text = state["text"]
    history = state.get("history",[])
    # 🧠 Convert history into readable format
    history_text = ""
    for item in history:
        history_text += f"- {item['action']} → {item.get('target', '')}\n"

    enhanced_input = f"""
    Previous actions:
    {history_text}

    User request:
    {user_text}
    """


    result = generate_command(enhanced_input)
    print("\n🧠 LLM Output:\n", result)

    if result.get("action") == "none":
        state["error"] = "invalid_or_unsafe_request"
        return state

    state["plan"] = result
    return state


# 🔐 Validator Node
ALLOWED_ACTIONS = [
    "create_file",
    "create_folder",
    "list_files",
    "rename_file",
    "rename_folder",
    "append_file",
    "overwrite_file"
]


def validator_node(state):
    if "error" in state:
        return state

    plan = state.get("plan", {})
    action = plan.get("action")

    if action not in ALLOWED_ACTIONS:
        print(f"🚫 Invalid action: {action}")
        state["error"] = "invalid_action"
        return state

    target = plan.get("target", "")

    if target:
        if ".." in target or target.startswith("/") or ":" in target:
            print("🚫 Unsafe path detected")
            state["error"] = "unsafe_path"
            return state

    print("✅ Validation Passed")
    return state


# ⚙️ Executor Node
def executor_node(state):
    if "error" in state:
        print("⚠️ Execution skipped:", state["error"])
        return state

    plan = state["plan"]

    print(f"⚙️ Executing: {plan}")
    result = execute_plan(plan)

    print(result)
     # 🧠 Store memory
    history = state.get("history", [])
    history.append({
        "action": plan.get("action"),
        "target": plan.get("target")
    })

    # Keep only last 5 actions 
    state["history"] = history[-5:]
    state["result"] = result
    return state


# 🔄 Build Graph
def build_graph(checkpointer=None):
    graph = StateGraph(State)

    graph.add_node("input", input_node)
    graph.add_node("planner", planner_node)
    graph.add_node("validator", validator_node)
    graph.add_node("executor", executor_node)

    graph.set_entry_point("input")

    graph.add_edge("input", "planner")
    graph.add_edge("planner", "validator")
    graph.add_edge("validator", "executor")

    return graph.compile(checkpointer=checkpointer)