import os

BASE_DIR = "./workspace"

# Ensure workspace exists
os.makedirs(BASE_DIR, exist_ok=True)


def safe_path(path: str):
    if not path:
        return None

    if ".." in path or path.startswith("/") or ":" in path:
        return None

    return os.path.join(BASE_DIR, path)


def execute_plan(plan: dict):
    action = plan.get("action")
    target = plan.get("target", "")
    content = plan.get("content", "")

    path = safe_path(target)

    if action == "create_file":
        if not path:
            return "❌ Unsafe file path"

        with open(path, "w") as f:
            f.write(content or "")

        return f"✅ File created: {target}"

    elif action == "create_folder":
        if not path:
            return "❌ Unsafe folder path"

        os.makedirs(path, exist_ok=True)
        return f"✅ Folder created: {target}"

    elif action == "list_files":
        files = os.listdir(BASE_DIR)
        return f"📂 Files: {files}"

    elif action == "none":
        return "⚠️ No valid action from LLM"

    return "❌ Unknown action"