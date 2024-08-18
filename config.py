import json


def read(file="config.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {}

def write(data,file="config.json"):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
if __name__ == "__main__":
    print(read())
