from speech_to_text import listen_command
from langgraph_flow import build_graph
from langgraph.checkpoint.mongodb import MongoDBSaver

with MongoDBSaver.from_conn_string(
    "mongodb://localhost:27017/",
    db_name="voice_agent",
    collection_name="checkpoints"
) as checkpointer:

    app = build_graph(checkpointer=checkpointer)
    while True:
        command = listen_command()
        if command is None:
            continue
        if "exit" in command:
            print("Exiting CLI...")
            break
        app.invoke(
            {"text" : command,},
            config={
                "configurable":{
                    "thread_id": "voice_session-1"
                }
            }
        )
