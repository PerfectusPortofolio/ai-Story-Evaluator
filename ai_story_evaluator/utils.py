import json


def save_results(data, filename="analysis.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
