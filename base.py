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