import json

def read():
    try:
        with open('config/config.json', 'r') as f:
            return json.load(f)
    except:
        return {}

if __name__ == '__main__':
    print(read())