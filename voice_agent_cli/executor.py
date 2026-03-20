import os

BASE_DIR = "./workspace"
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
    new_name = plan.get("new_name", "")
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

    elif action == "rename_file":
        new_path = safe_path(new_name)

        if not path or not new_path:
            return "❌ Unsafe rename"

        if not os.path.exists(path):
            return "❌ File does not exist"

        os.rename(path, new_path)
        return f"✅ Renamed file {target} → {new_name}"

    elif action == "rename_folder":
        new_path = safe_path(new_name)

        if not path or not new_path:
            return "❌ Unsafe rename"

        if not os.path.exists(path):
            return "❌ Folder does not exist"

        os.rename(path, new_path)
        return f"✅ Renamed folder {target} → {new_name}"

    elif action == "append_file":
        if not path:
            return "❌ Unsafe file path"

        with open(path, "a") as f:
            f.write(content)

        return f"✅ Appended to {target}"

    elif action == "overwrite_file":
        if not path:
            return "❌ Unsafe file path"

        with open(path, "w") as f:
            f.write(content)

        return f"✅ Overwritten {target}"

    elif action == "none":
        return "⚠️ No valid action"

    return "❌ Unknown action"