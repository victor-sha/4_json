import json
import sys


def load_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file_handler:
            if not file_handler:
                raise Exception("File is empty")                
            else:
                return file_handler.read()
    except FileNotFoundError:
        print("Wrong file or file path")


def pretty_print_json(data):
    json_obj = json.loads(data)
    return json.dumps(json_obj, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    print(pretty_print_json(data))
