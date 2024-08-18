from qcloud_cos import CosConfig, CosS3Client
import config
from datetime import datetime
import os,base

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





def upload(cf:dict,force=""):
    if force=="":
        force = cf["force"]
    base.log("开始上传流程")
    if not force:
        if base.file_hash(cf["file_path"]) == config.read("auto.json")["old_hash"]:
            base.log("文件未改变，不上传")
            return {}
        else:
            ac = config.read("auto.json")
            ac["old_hash"] = base.file_hash(cf["file_path"])
            base.log(ac)
            
            base.log("检测到文件改变，开始上传")
    else:
        base.log("正在强制上传")
            
    # 读取密码配置
    kf = config.read("key.json")

    client = CosS3Client(CosConfig(Region=cf["region"], SecretId=kf["secret_id"], SecretKey=kf["secret_key"]))
    response = client.put_object_from_local_file(
        Bucket=cf["bucket"],
        LocalFilePath=cf["file_path"],
        Key=timekey(cf["head"],cf["file_name"]),
        EnableMD5=False,
        StorageClass=cf["storage_class"],
    )
    return response,base.file_hash(cf["file_path"])
