import json


def save_json(data, json_file_name):
    with open(json_file_name, "w") as f:
        json.dump(data, f, indent=4)


def load_json(json_file_name):
    with open(json_file_name, "r") as f:
        data = json.load(f)
    return data


def load_txt(txt_file_name):
    with open(txt_file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines
