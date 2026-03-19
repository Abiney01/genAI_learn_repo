from speech_to_text import listen_command
from langgraph_flow import build_graph
from langgraph.checkpoint.mongodb import MongoDBSaver


def main():
    print("🎙️ Voice CLI Agent Started (say 'exit' to quit)\n")

    with MongoDBSaver.from_conn_string(
        "mongodb://localhost:27017/",
        db_name="voice_agent",
        collection_name="checkpoints"
    ) as checkpointer:

        app = build_graph(checkpointer=checkpointer)

        while True:
            try:
                command = listen_command()

                if not command:
                    continue

                if "exit" in command.lower():
                    print("👋 Exiting CLI...")
                    break

                # 🔄 Invoke LangGraph
                result = app.invoke(
                    {"text": command},
                    config={
                        "configurable": {
                            "thread_id": "voice_session-2"
                        }
                    }
                )

                # 📤 Print final result
                if result.get("result"):
                    print(f"\n✅ Result: {result['result']}")
                elif result.get("error"):
                    print(f"\n❌ Error: {result['error']}")
                else:
                    print("\n⚠️ No output returned")

            except KeyboardInterrupt:
                print("\n👋 Interrupted. Exiting...")
                break

            except Exception as e:
                print(f"\n🔥 Unexpected Error: {str(e)}")


if __name__ == "__main__":
    main()