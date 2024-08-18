import datetime,config,hashlib,os

ld = config.read()["log"]

ldl = {
    0:"Debug",
    1:"Info",
    2:"Warn",
    3:"Error"
}

def log(text,iew=1):
    if iew >= ld:
        print(f"""[{datetime.datetime.now().strftime(r"%y/%m/%d %H:%M:%S")}][{ldl[iew]}] {text}""")
        return True
    return False

def file_hash(file_path: str, hash_method=hashlib.sha256) -> str:
    if not os.path.isfile(file_path):
        return ''
    h = hash_method()
    with open(file_path, 'rb') as f:
        while b := f.read(8192):
            h.update(b)
    return h.hexdigest()

def dict_to_seconds(time_dict:dict):
    seconds_per_minute = 60
    seconds_per_hour = 3600
    seconds_per_day = 86400  # 24 * 60 * 60
    seconds_per_week = 604800  # 7 * 24 * 60 * 60
    seconds_per_month = 2592000  # 30 * 24 * 60 * 60

    total_seconds = 0
    total_seconds += time_dict.get("sec", 0)
    total_seconds += time_dict.get("min", 0) * seconds_per_minute
    total_seconds += time_dict.get("hour", 0) * seconds_per_hour
    total_seconds += time_dict.get("day", 0) * seconds_per_day
    total_seconds += time_dict.get("week", 0) * seconds_per_week
    total_seconds += time_dict.get("mon", 0) * seconds_per_month

    return total_seconds

def conl():
    return os.path.exists("config.json"),os.path.exists("key.json"),os.path.exists("ac.json")