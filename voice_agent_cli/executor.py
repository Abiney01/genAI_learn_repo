import os

# ❌ Commands we DO NOT auto-execute
BLOCKED_KEYWORDS = [
    "npm start",
    "npm run",
    "python app.py",
    "python main.py",
    "uvicorn",
    "flask run",
    "streamlit run"
]


def is_safe_to_execute(command: str) -> bool:
    for keyword in BLOCKED_KEYWORDS:
        if keyword in command.lower():
            return False
    return True


def execute_command(command: str):
    print(f"\n🛠 Command: {command}")

    if not is_safe_to_execute(command):
        print("⚠️ Skipped execution (manual run required)")
        return

    print("⚡ Executing...\n")

    try:
        result = os.system(command)
        print("✅ Done\n")
        return result
    except Exception as e:
        print(f"❌ Execution error: {e}")