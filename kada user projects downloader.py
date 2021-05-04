# Scratch Source Downloader V0.1
# By TimFang4162
# Warning:
#    only for learning and communication
#    Please do not use for illegal purposes
#    All consequences are at your own risk
# How to use:
#    Double click to run this program
#    Please do not open in IDLE
import json
import zipfile
import requests
import os
import time

#kada user project downloader

httpsession = requests.session()
uid = input("kada uid? ")  #81002
upr = json.loads(
    httpsession.get(
        url=
        "https://kada.163.com/j/user/project/publish/list.json?limit=10&offset=0&pageIndex=1&pageSize=100&relativeOffset=0&uid="
        + uid).text)['result']['list']
for projects in upr:
    projects = str(projects['id'])
    project_url = "https://kada.163.com/project/" + projects + "-" + uid + ".htm"
    starttime = time.time()
    project_htm = httpsession.get(url=project_url)
    project_name = project_htm.text[project_htm.text.find('<title>') +
                                    7:project_htm.text.find('网易有道卡搭</title>')]
    temp = project_htm.text.find('"projectUrl": "\//steam.nosdn.127.net/')
    print("Project name:", project_name)
    if (project_htm.text[temp + 33 + 38:temp + 37 + 38] == "json"):
        print("Project version: 3.0")
        f_out = open(project_name + ".sb3", "w")
        f_out.close()
        f_out = zipfile.ZipFile(project_name + ".sb3", "w")
        project_json = httpsession.get(
            url="https://steam.nosdn.127.net/" +
            project_htm.text[temp + 38:temp + 37 + 38]).text
        f_out.writestr("project.json", data=project_json, compress_type=8)
        project_json = json.loads(project_json)['targets']
        project_md5_list = []
        for project_costume in project_json:
            for project_costume_md5 in project_costume['costumes']:
                project_md5_list.append(project_costume_md5['md5ext'])
        for project_sound in project_json:
            for project_sound_md5 in project_sound['sounds']:
                project_md5_list.append(project_sound_md5['md5ext'])
        project_md5_list = list(set(project_md5_list))
        md5num = 1
        for md5 in project_md5_list:
            print("Downloading: ",
                  md5,
                  " (",
                  md5num,
                  "/",
                  len(project_md5_list),
                  ")",
                  sep="")
            f_out.writestr(
                md5,
                data=httpsession.get("https://steam.nosdn.127.net/" +
                                     md5).content,
                compress_type=8)
            md5num = md5num + 1
        f_out.close()
        print("Time:", str(time.time() - starttime) + "s")
    else:

        # Scratch 2.0 DEMO
        # Bug Bug Bug
        # Do not run this

        print("Project version: 2.0")
        f_out = open(project_name + ".sb2", "wb")
        f_out.write(
            requests.get(url="https://steam.nosdn.127.net/" +
                         project_htm.text[temp + 38:temp + 37 + 37]).content)
        f_out.close()
        print("Time:", str(time.time() - starttime) + "s")
    print("")