import os


def load_python_files(path):
    python_files = []

    if os.path.isfile(path) and path.endswith(".py"):
        return [path]

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    return python_files
