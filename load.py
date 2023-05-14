import sys
import shutil
import json
import calendar
import time
import os

buildId = sys.argv[1]
print(buildId)
versionName = sys.argv[2]
print(versionName)
versionCode = sys.argv[3]
print(versionCode)
packageName = sys.argv[4]
print(packageName)
description = sys.argv[5]
print(description)
fileSrc = sys.argv[6]
print(fileSrc)

timeStamp = calendar.timegm(time.gmtime())

apkDir = os.getcwd() + "/apks"
apkName = "/app_release_" + buildId + "_" + versionCode + ".apk"
apkDest = apkDir + apkName

if not os.path.exists(apkDir):
    os.makedirs(apkDir)

print("copy " + fileSrc + "to" + apkDest)

shutil.copyfile(fileSrc, apkDest)

with open('app.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

print('get json data: ',json_data)

info = {
    "build_id": buildId, 
    "version_name": versionName, 
    "version_code": versionCode, 
    "package_name": packageName, 
    "update_description": description, 
    "create_time": timeStamp, 
    "download_url": "/apks" + apkName
}

print('add json data: ',info)

list = json_data["data"]
length = len(list)

if length > 9:
    del list[length - 1]
else:
    length = length + 1

json_data["count"] = length
list.insert(0, info)

with open('app.json','w',encoding='utf8')as fp:
    json.dump(json_data,fp,ensure_ascii=False)

print('update scuuess')
