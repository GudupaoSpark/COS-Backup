import config,base,os,sys,cos,time

# 读取配置
cf = config.read()

# 初始化
if __name__ == "__main__":
    print(r"""   ____ ___  ____        ____             _                
  / ___/ _ \/ ___|      | __ )  __ _  ___| | ___   _ _ __  
 | |  | | | \___ \ _____|  _ \ / _` |/ __| |/ / | | | '_ \ 
 | |__| |_| |___) |_____| |_) | (_| | (__|   <| |_| | |_) |
  \____\___/|____/      |____/ \__,_|\___|_|\_\\__,_| .__/ 
                                                    |_|    
https://github.com/GudupaoSpark/COS-Backup
Copyright (c) 2024 Gudupao
""")
    c = base.conl()
    if c[0] and c[1]:
        base.log("配置文件正常！")
    else:
        if not c[0] and not c[1]:
            base.log("缺少配置文件 config.json, key.json",3)
        elif not c[0]:
            base.log("缺少配置文件 config.json",3)
        elif not c[1]:
            base.log("缺少配置文件 key.json",3)
        base.log("启动失败",3)
        os._exit(1)
    
    if not c[2]:
        base.log("缺少运行时文件 ac.json 正在自动创建 ",2)
        config.write({"old_hash":""},"ac.json")
        base.log("已创建 ac.json ",0)
    else:
        base.log("运行时文件正常！",1)
    
    if not os.path.exists(cf["file_path"]):
        base.log("要备份的文件不存在",3)
        os._exit(1)
    
    cf = config.read()
    
    base.log("启动成功")
    
    if "now" in sys.argv:
        base.log("单次模式",1)
        cos.upload(cf,force=True)
        base.log("上传完成",1)
        os._exit(0)
    
    base.log("正常模式",1)
    ot = time.time()
    
        