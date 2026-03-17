from speech_to_text import listen_command
from langgraph_flow import build_graph

app = build_graph()
while True:
    command = listen_command()
    if command is None:
        continue
    if "exit" in command:
        print("Exiting CLI...")
        break
    app.invoke({
        "text" : command
    })
