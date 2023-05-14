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

fileUrl = "/apks/app_" + buildId + "_" + versionCode + ".apk"
apkDest = os.getcwd() + fileUrl

if not os.path.exists(apkDest):
    os.makedirs(apkDest)

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
    "download_url": fileUrl
}

print('add json data: ',info)

json_data["count"] = json_data["count"] + 1
json_data["data"].insert(0, info)

with open('app.json','w',encoding='utf8')as fp:
    json.dump(json_data,fp,ensure_ascii=False)

print('update scuuess')
