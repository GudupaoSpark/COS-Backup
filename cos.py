from qcloud_cos import CosConfig, CosS3Client
import config
from datetime import datetime
import os

# 读取配置
cf = config.read()
kf = config.read("key.json")


# 文件链接生成
def timekey(
    head:str="Backup",
    end:str="backup",
    dir:bool=True
):
    if dir:
        formatted_string = datetime.now().strftime(f"{head}/%y/%m/%d/%H-%M-%S-{end}")
    else:
        formatted_string = datetime.now().strftime(f"{head}/%y-%m-%d-%H-%M-%S-{end}")
    return formatted_string


secret_id = kf["secret_id"]
secret_key = kf["secret_key"]
region = cf["region"]

client = CosS3Client(CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key))


def upload():
    response = client.put_object_from_local_file(
        Bucket=cf["bucket"],
        LocalFilePath=cf["file"],
        Key=timekey(cf["file"]),
        EnableMD5=False,
        StorageClass=cf["storage_class"],
    )
    return response
